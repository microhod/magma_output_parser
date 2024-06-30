# To run the script
#  - download python 3: https://www.python.org/downloads/
#  - or check your local version of python in the terminal
#       python --version
#  - now run the script in the terminal
#       python parse.py "/path/to/input.txt" "/path/to/output_directory/"
#
# Note: if you don't supply an output directory, the script will default to outputting to the current directory
import csv_writer
import magma_parser.parser as magma_parser
from models import GaloisInfo, Group, GroupPermutationRepresentation, GroupRepresentation, Permutation, normalise_group_galois_types
import sys


def parse_group(record: magma_parser.Record) -> Group:
    isom: magma_parser.GroupRep = record.fields.get('isom')
    if isom is None:
        raise ValueError("expected field 'isom'")

    # perm_isom is optional
    perm_isom = record.fields.get('perm_isom')

    equiv_rep: magma_parser.GroupRepDesc = record.fields.get('equiv_rep')
    if isom is None:
        raise ValueError("expected field 'equiv_rep'")

    galois_field = record.fields.get('HGS_GN')
    if galois_field is None:
        galois_field = record.fields.get('sbracoid_GN')
    if galois_field is None:
        raise ValueError("expected galois field 'HGS_GN' or 'sbracoid_GN'")

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
        perm_isom=perm_isom,
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
        csv_writer.to_csv(groups, output_dir)
