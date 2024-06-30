import xlsxwriter
from xlsxwriter import Workbook
from xlsxwriter.worksheet import Worksheet

from models import Group

def write(groups: list[Group], output_dir: str):
    if len(groups) == 0:
        return
    
    # ensure groups are sorted by isometry
    groups.sort(key=lambda g: g.isom)

    galois_types = list(groups[0].galois.keys())
    n = -1
    for type in list(groups[0].galois.keys()):
        # get the order of the group list
        n = groups[0].galois[type][0].type.n
        break

    with xlsxwriter.Workbook(f'{output_dir}/groups_{n}.xlsx') as workbook:
        for type in galois_types:
            sheet = workbook.add_worksheet(type)
            _write_galois_type(workbook, sheet, groups, type)


def _write_galois_type(book: Workbook, sheet: Worksheet, groups: list[Group], galois_type: str):
    # construct header
    header = ["group", "isom"]
    # check first group to decide if we should include perm_isom
    if groups[0].perm_isom:
        header.append("perm_isom")

    non_galois_headers = len(header)
    
    # we assume there is at least 1 group and at least 1 galois info for each group.
    galois_keys = [key for key in groups[0].galois[galois_type][0].nums.keys()]
    for galois in groups[0].galois[galois_type]:
        header.extend([f"{galois.type}.{key}" for key in galois_keys])
        pass

    for i, name in enumerate(header):
        fmt = book.add_format()
        fmt.set_border()
        fmt.set_border_color('gray')
        # put thick black borders around galois fields
        if i >= non_galois_headers:
            fmt.set_top(5)
            fmt.set_top_color('black')
            if (i - non_galois_headers) % len(galois_keys) == 0:
                fmt.set_left(5)
                fmt.set_left_color('black')
            if (i - non_galois_headers) % len(galois_keys) == len(galois_keys)-1:
                fmt.set_right(5)
                fmt.set_right_color('black')

        sheet.write(0, i, name, fmt)

    row_num = 1
    for g in groups:
        row = [g.perm_rep, g.isom]
        if "perm_isom" in header:
            row.append(g.perm_isom)
        for galois in g.galois[galois_type]:
            row.extend(galois.nums[key] for key in galois_keys)

        row = [str(x) for x in row]
        for i, x in enumerate(row):
            fmt = book.add_format()
            fmt.set_border()
            fmt.set_border_color('gray')

            # grey out zero fields
            if x == "0":
                fmt.set_bg_color('#D0CFD0')
            # put thick black borders around galois fields
            if i >= non_galois_headers:
                if (i - non_galois_headers) % len(galois_keys) == 0:
                    fmt.set_left(5)
                    fmt.set_left_color('black')
                if (i - non_galois_headers) % len(galois_keys) == len(galois_keys)-1:
                    fmt.set_right(5)
                    fmt.set_right_color('black')
                if i >= non_galois_headers and row_num == len(groups):
                    fmt.set_bottom(5)
                    fmt.set_bottom_color('black')

            sheet.write(row_num, i, x, fmt)

        row_num += 1

