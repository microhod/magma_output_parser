import xlsxwriter
from xlsxwriter import Workbook
from xlsxwriter.worksheet import Worksheet

from models import Group

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
    # construct header
    header = ["group", "isom"]
    # check first group to decide the rest of the header
    g = groups[0]
    if g.perm_id:
        header.append("perm_isom")

    non_structure_headers = len(header)
    
    # we assume there is at least 1 structure for each group.
    structure_reps = sorted(g.structures.keys())
    property_keys = list(g.structure_property_keys(property_type))
    for rep in structure_reps:
        header.extend([f"{rep}.{key}" for key in property_keys])

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

        sheet.write(0, i, name, fmt)

    row_num = 1
    for g in groups:
        row = [g.perm_rep, g.isom_rep]
        if "perm_isom" in header:
            row.append(g.perm_id)
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
                if i >= non_structure_headers and row_num == len(groups):
                    fmt.set_bottom(5)
                    fmt.set_bottom_color('black')

            sheet.write(row_num, i, x, fmt)

        row_num += 1

