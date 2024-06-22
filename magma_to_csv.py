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
class GroupHgs:
    type: GroupRepresentation
    tot: int
    gal: int
    ac: int
    bc: int


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
    hgs: list[GroupHgs]


def deduplicate_hgs(hgs_list: list[GroupHgs]) -> list[GroupHgs]:
    deduped = []
    seen_types = set()
    for hgs in hgs_list:
        if hgs.type in seen_types:
            continue

        seen_types.add(hgs.type)
        deduped.append(hgs)

    return deduped


# normalise_group ensures all groups have the same hgs types, with any missing types
# added in with zero'd GN values
def normalise_group_hgs_types(groups: list[Group]) -> list[Group]:
    # sort groups by their isometry
    groups.sort(key=lambda g: g.isom)

    # get sorted list of all hgs types and sort all group hgs types
    # so they can be compared index by index
    hgs_types = set()
    for group in groups:
        # hgs can be duplicated, so we should remove duplicates
        group.hgs = deduplicate_hgs(group.hgs)

        hgs_types.update([hgs.type for hgs in group.hgs])
        group.hgs.sort(key=lambda hgs: hgs.type)

    all_hgs_types = list(hgs_types)
    all_hgs_types.sort()

    for group in groups:
        for i, type in enumerate(all_hgs_types):
            if i < len(group.hgs) and group.hgs[i].type == type:
                continue

            # insert missing type with zero GN values at the correct index
            zero_hgs = GroupHgs(type=type, tot=0, gal=0, ac=0, bc=0)
            group.hgs = group.hgs[:i] +[zero_hgs] + group.hgs[i:]

    return groups


# groups_to_csv writes the list of groups to a csv file
def groups_to_csv(groups: list[Group], output_dir: str):
    if len(groups) == 0:
        return
    
    # ensure groups are sorted by isometry
    groups.sort(key=lambda g: g.isom)
    
    # get the order of the group list
    n = groups[0].hgs[0].type.n
    output_file = os.path.join(output_dir, f"groups_{n}.csv")

    # construct CSV header
    header = ["group", "isom"]
    types = [hgs.type for hgs in groups[0].hgs]
    for type in types:
        header.extend([f"{type}.tot", f"{type}.gal", f"{type}.ac", f"{type}.bc"])
    
    # have to set newline="" because otherwise windows gets blank lines
    # https://stackoverflow.com/a/3348664
    with open(output_file, "+w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)

        for g in groups:
            row = [g.perm_rep, g.isom]
            for hgs in g.hgs:
                row.extend([hgs.tot, hgs.gal, hgs.ac, hgs.bc])
            w.writerow(row)


def parse_group(record: magma_parser.Record) -> Group:
    isom: magma_parser.GroupRep = record.fields.get('isom')
    if isom is None:
        raise ValueError("expected field 'isom'")

    equiv_rep: magma_parser.GroupRepDesc = record.fields.get('equiv_rep')
    if isom is None:
        raise ValueError("expected field 'equiv_rep'")

    hgs_gns = record.fields.get('HGS_GN')
    if hgs_gns is None:
        raise ValueError("expected field 'HGS_GN'")

    hgs = []
    for hgs_gn in hgs_gns:
        record: magma_parser.Record = hgs_gn[0]
        group_rep: magma_parser.GroupRep = hgs_gn[1]

        hgs.append(GroupHgs(
            GroupRepresentation(group_rep.n, group_rep.x),
            record.fields['tot'],
            record.fields['gal'],
            record.fields['ac'],
            record.fields['bc'],
        ))

    return Group(
        isom=GroupRepresentation(isom.n, isom.x),
        perm_rep=GroupPermutationRepresentation(
            perms=[Permutation(p.parts) for p in equiv_rep.permutations]
        ),
        hgs=hgs
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
        groups = normalise_group_hgs_types(groups)
        groups_to_csv(groups, output_dir)
