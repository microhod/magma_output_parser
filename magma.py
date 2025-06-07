# To run the script
#  - download python 3: https://www.python.org/downloads/
#  - or check your local version of python in the terminal
#       python --version
#  - now run the script in the terminal
#       python parse.py "/path/to/input.txt" "/path/to/output_directory/"
#
# Note: if you don't supply an output directory, the script will default to outputting to the current directory
import sys

import csv_writer
import magma_parser.parser as magma_parser
from models import GaloisInfo, Group, GroupPermutationRepresentation, GroupRepresentation, GroupStructure, Permutation, normalise_group_galois_types
import xlsx_writer


def parse_group(record: magma_parser.Record) -> Group:
    isom: magma_parser.GroupRep = record.fields.get('isomtype') or record.fields.get('isom')
    if isom is None:
        raise ValueError("expected field 'isomtype' or 'isom'")

    perm_id = record.fields.get('permID') or record.fields.get('perm_isom')
    soluble = record.fields.get('Gsol')

    perm_rep: magma_parser.GroupRepDesc = record.fields.get('equiv_rep')
    if 'structures' in record.fields:
        perm_rep = record.fields.get('structures')[0].fields.get('group')

    structures = {}
    for sub_record in record.fields.get('structures', []):
        sub_record_type = sub_record.fields.get('type')
        id_type: magma_parser.GroupRep = sub_record_type.fields.get('IDtype')

        structures[GroupRepresentation(id_type.n, id_type.x)] = GroupStructure(
            properties={
                'hgs': sub_record.fields.get('HGS').fields,
                'bracoid': sub_record.fields.get('SB').fields,
            },
            soluble=sub_record_type.fields.get('Nsol'),
        )

    # backwards compatibility with old non-structred record layout
    for elem in record.fields.get('HGS_GN', []):
        sub_record: magma_parser.Record = elem[0]
        rep = GroupRepresentation(elem[1].n, elem[1].x)

        if rep not in structures:
            structures[rep] = GroupStructure(properties={})
        structures[rep].properties['hgs'] = sub_record.fields
    for elem in record.fields.get('sbracoid_GN', []):
        sub_record: magma_parser.Record = elem[0]
        rep = GroupRepresentation(elem[1].n, elem[1].x)

        if rep not in structures:
            structures[rep] = GroupStructure(properties={})
        structures[rep].properties['bracoid'] = sub_record.fields    

    # TODO: remove all 'galois' references
    galois_fields = {}
    if record.fields.get('HGS_GN'):
        galois_fields['hgs'] = record.fields.get('HGS_GN')
    if record.fields.get('sbracoid_GN'):
        galois_fields['bracoid'] = record.fields.get('sbracoid_GN')

    galois_infos = {}
    for type in galois_fields:
        galois_infos[type] = []

        for field in galois_fields[type]:
            sub_record: magma_parser.Record = field[0]
            group_rep: magma_parser.GroupRep = field[1]

            galois_infos[type].append(GaloisInfo(
                type=GroupRepresentation(group_rep.n, group_rep.x),
                nums=sub_record.fields
            ))

    return Group(
        perm_rep=GroupPermutationRepresentation(
            perms=[Permutation(p.parts) for p in perm_rep.permutations]
        ),
        perm_id=perm_id,
        isom_rep=GroupRepresentation(isom.n, isom.x),
        soluble=soluble,
        structures=structures,
        galois=galois_infos,
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


def magma(input_file, output_dir, writer):
    for groups in parse(input_file):
        groups = normalise_group_galois_types(groups)

        match writer:
            case "csv":
                csv_writer.write(groups, output_dir)
            case "xlsx":
                xlsx_writer.write(groups, output_dir)
            case "stdout":
                for g in groups:
                    print(g)
            case _:
                raise ValueError(f'unsupported writer [{writer}]')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("please provide the file you would like to parse")
        exit(1)

    input_file = sys.argv[1]
    output_dir = "."  # default to the current directory
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    writer = "xlsx"
    if len(sys.argv) > 3:
        writer = sys.argv[3]

    magma(input_file, output_dir, writer)
