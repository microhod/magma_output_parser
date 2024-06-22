# To run the script
#  - download python 3: https://www.python.org/downloads/
#  - or check your local version of python in the terminal
#       python --version
#  - now run the script in the terminal
#       python parse.py "/path/to/input.txt" "/path/to/output_directory/"
#
# Note: if you don't supply an output directory, the script will default to outputting to the current directory
import csv
from dataclasses import dataclass
import os
import magma_parser.parser as magma_parser
import sys


@dataclass
class GroupRepresentation:
    n: int
    x: int

    def __str__(self) -> str:
        if self.n == 0 and self.x == 0:
            return "unknown"
        return f"<{self.n}:{self.x}>"

    def __hash__(self) -> int:
        return hash(str(self))
    
    def __eq__(self, other):
        return self.n == other.n and self.x == other.x
    
    def __lt__(self, other):
        return self.n < other.n or (self.n == other.n and self.x < other.x)


@dataclass
class GaloisInfo:
    type: GroupRepresentation
    nums: dict[str, int]


@dataclass
class Permutation:
    parts: list[tuple[int]]

    def __str__(self) -> str:
        s = ""
        for part in self.parts:
            s += '(' + ','.join([str(p) for p in part]) + ')'
        return s


@dataclass
class GroupPermutationRepresentation:
    perms: list[Permutation]

    def __str__(self) -> str:
        return '<' + ', '.join([str(p) for p in self.perms]) + '>'


@dataclass
class Group:
    isom: GroupRepresentation
    perm_rep: GroupPermutationRepresentation
    galois: list[GaloisInfo]


def deduplicate_galois_infos(galois_infos: list[GaloisInfo]) -> list[GaloisInfo]:
    deduped = []
    seen_types = set()
    for info in galois_infos:
        if info.type in seen_types:
            continue

        seen_types.add(info.type)
        deduped.append(info)

    return deduped


# normalise_group ensures all groups have the same galois types, with any missing types
# added in with zero'd GN values
def normalise_group_galois_types(groups: list[Group]) -> list[Group]:
    # sort groups by their isometry
    groups.sort(key=lambda g: g.isom)

    # get sorted list of all galois types and sort all group galois types
    # so they can be compared index by index
    galois_types = set()
    for group in groups:
        # galois can be duplicated, so we should remove duplicates
        group.galois = deduplicate_galois_infos(group.galois)

        galois_types.update([galois.type for galois in group.galois])
        group.galois.sort(key=lambda galois: galois.type)

    all_galois_types = list(galois_types)
    all_galois_types.sort()

    for group in groups:
        for i, type in enumerate(all_galois_types):
            if i < len(group.galois) and group.galois[i].type == type:
                continue

            # we assume there is at least 1 galois info for each group.
            num_keys = list(group.galois[0].nums.keys())

            # insert missing type with zero GN values at the correct index
            zero_galois = GaloisInfo(type=type, nums={key: 0 for key in num_keys})
            group.galois = group.galois[:i] +[zero_galois] + group.galois[i:]

    return groups


# groups_to_csv writes the list of groups to a csv file
def groups_to_csv(groups: list[Group], output_dir: str):
    if len(groups) == 0:
        return
    
    # ensure groups are sorted by isometry
    groups.sort(key=lambda g: g.isom)
    
    # get the order of the group list
    n = groups[0].galois[0].type.n
    output_file = os.path.join(output_dir, f"groups_{n}.csv")

    # construct CSV header
    header = ["group", "isom"]
    # we assume there is at least 1 group and at least 1 galois info for each group.
    galois_keys = [key for key in groups[0].galois[0].nums.keys()]
    for galois in groups[0].galois:
        header.extend([f"{galois.type}.{key}" for key in galois_keys])
        pass
    
    # have to set newline="" because otherwise windows gets blank lines
    # https://stackoverflow.com/a/3348664
    with open(output_file, "+w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)

        for g in groups:
            row = [g.perm_rep, g.isom]
            for galois in g.galois:
                row.extend(galois.nums[key] for key in galois_keys)
            w.writerow(row)


def parse_group(record: magma_parser.Record) -> Group:
    isom: magma_parser.GroupRep = record.fields.get('isom')
    if isom is None:
        raise ValueError("expected field 'isom'")

    equiv_rep: magma_parser.GroupRepDesc = record.fields.get('equiv_rep')
    if isom is None:
        raise ValueError("expected field 'equiv_rep'")

    galois_field = record.fields.get('HGS_GN')
    if galois_field is None:
        raise ValueError("expected field 'HGS_GN'")

    galois_infos = []
    for field in galois_field:
        record: magma_parser.Record = field[0]
        group_rep: magma_parser.GroupRep = field[1]

        galois_infos.append(GaloisInfo(
            type=GroupRepresentation(group_rep.n, group_rep.x),
            nums=record.fields
        ))

    return Group(
        isom=GroupRepresentation(isom.n, isom.x),
        perm_rep=GroupPermutationRepresentation(
            perms=[Permutation(p.parts) for p in equiv_rep.permutations]
        ),
        galois=galois_infos
    )


def parse(filepath: str) -> list[list[Group]]:
    group_lists = []
    record_outputs = magma_parser.parse_file(filepath)

    for i, record_output in enumerate(record_outputs):
        groups = []
        for j, record in enumerate(record_output):
            try:
                groups.append(parse_group(record))
            except ValueError as e:
                raise ValueError(f"output[{i}], record[{j}]: {e}")
        group_lists.append(groups)

    return group_lists


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("please provide the file you would like to parse")
        exit(1)

    input_file = sys.argv[1]
    output_dir = "."  # default to the current directory
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]

    for groups in parse(input_file):
        groups = normalise_group_galois_types(groups)
        groups_to_csv(groups, output_dir)
