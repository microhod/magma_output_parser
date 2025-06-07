import csv
import os

from models import Group

# writes the list of groups to a csv file
def write(groups: list[Group], output_dir: str):
    if len(groups) == 0:
        return
    
    # ensure groups are sorted by isometry
    groups.sort(key=lambda g: g.isom_rep)

    g = groups[0]
    for property_type in g.structure_property_types():
        output_file = os.path.join(output_dir, f"groups_{g.order()}_{property_type}.csv")
        _write_structure_type(groups, property_type, output_file)


def _write_structure_type(groups: list[Group], property_type: str, output_file):
    # construct CSV header
    header = ["group", "isom"]
    # check first group to decide the rest of the header
    g = groups[0]
    if g.perm_id is not None:
        header.append("perm_isom")
    # we assume there is at least 1 structure for each group.
    structure_reps = sorted(g.structures.keys())
    property_keys = list(g.structure_property_keys(property_type))
    for rep in structure_reps:
        header.extend([f"{rep}.{key}" for key in property_keys])
    
    # have to set newline="" because otherwise windows gets blank lines
    # https://stackoverflow.com/a/3348664
    with open(output_file, "+w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)

        for g in groups:
            row = [g.perm_rep, g.isom_rep]
            if "perm_isom" in header:
                row.append(g.perm_id)
            for rep in structure_reps:
                row.extend(g.structures[rep].properties[property_type][key] for key in property_keys)
            w.writerow(row)
