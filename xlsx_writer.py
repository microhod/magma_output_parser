import xlsxwriter
from xlsxwriter import Workbook
from xlsxwriter.worksheet import Worksheet

from models import Group, GroupRepresentation

def write(groups: list[Group], output_dir: str):
    if len(groups) == 0:
        return
    
    # ensure groups are sorted by isometry
    groups.sort(key=lambda g: g.isom_rep)

    g = groups[0]
    with xlsxwriter.Workbook(f'{output_dir}/groups_{g.order()}.xlsx') as workbook:
        for property_type in g.structure_property_types():
            sheet = workbook.add_worksheet(property_type)
            _write_structure_type(workbook, sheet, groups, property_type)


def _write_structure_type(book: Workbook, sheet: Worksheet, groups: list[Group], property_type: str):
    structure_reps = sorted(groups[0].structures.keys())
    property_keys = list(groups[0].structure_property_keys(property_type))
    header, non_structure_headers, header_rows = _write_header(
        book,
        sheet,
        groups[0],
        structure_reps,
        property_keys,
    )

    row_num = header_rows
    for g in groups:
        row = [g.perm_rep, g.isom_rep]
        if "perm_isom" in header:
            row.append(g.perm_id)
        if "gsol" in header:
            row.append(str(g.soluble).upper())
        for rep in structure_reps:
            row.extend(g.structures[rep].properties[property_type][key] for key in property_keys)

        row = [str(x) for x in row]
        for i, x in enumerate(row):
            fmt = book.add_format()
            fmt.set_border()
            fmt.set_border_color('gray')

            # grey out zero fields
            if x == "0":
                fmt.set_bg_color('#D0CFD0')
            # put thick black borders around structure fields
            if i >= non_structure_headers:
                if (i - non_structure_headers) % len(property_keys) == 0:
                    fmt.set_left(5)
                    fmt.set_left_color('black')
                if (i - non_structure_headers) % len(property_keys) == len(property_keys)-1:
                    fmt.set_right(5)
                    fmt.set_right_color('black')
                if i >= non_structure_headers and row_num == len(groups)+header_rows-1:
                    fmt.set_bottom(5)
                    fmt.set_bottom_color('black')

            sheet.write(row_num, i, x, fmt)

        row_num += 1


def _write_header(
    book: Workbook,
    sheet: Worksheet,
    group: Group,
    structure_reps: list[GroupRepresentation],
    property_keys: list[str],
) -> tuple[list[str], int, int]:
    # construct header
    header = ["group", "isom"]
    # check first group to decide the rest of the header
    if group.perm_id is not None:
        header.append("perm_isom")
    if group.soluble is not None:
        header.append("gsol")
    # record non structure headers
    non_structure_headers = len(header)
    for rep in structure_reps:
        header.extend([f"{rep}.{key}" for key in property_keys])

    row = 0
    if group.has_structure_solublity():
        sheet.merge_range(row, 0, row, non_structure_headers - 1, "nsol", book.add_format({'align': 'center'}))

        border_center = book.add_format({'align': 'center', 'border': 5, 'border_color': 'black'})
        rep_index = 0
        for i in range(non_structure_headers, len(header)):
            if (i - non_structure_headers) % len(property_keys) == 0:
                structure = group.structures[structure_reps[rep_index]]
                soluble = str(structure.soluble).upper()
                sheet.merge_range(row, i, row, i + len(property_keys) - 1, soluble, border_center)
                rep_index += 1
        row += 1

    for i, name in enumerate(header):
        fmt = book.add_format()
        fmt.set_border()
        fmt.set_border_color('gray')
        # put thick black borders around stucture fields
        if i >= non_structure_headers:
            fmt.set_top(5)
            fmt.set_top_color('black')
            if (i - non_structure_headers) % len(property_keys) == 0:
                fmt.set_left(5)
                fmt.set_left_color('black')
            if (i - non_structure_headers) % len(property_keys) == len(property_keys)-1:
                fmt.set_right(5)
                fmt.set_right_color('black')

        sheet.write(row, i, name, fmt)
    
    return header, non_structure_headers, row+1