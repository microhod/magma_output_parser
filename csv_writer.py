import csv
import os

from models import Group

# to_csv writes the list of groups to a csv file
def to_csv(groups: list[Group], output_dir: str):
    if len(groups) == 0:
        return
    
    # ensure groups are sorted by isometry
    groups.sort(key=lambda g: g.isom)
    
    # get the order of the group list
    n = groups[0].galois[0].type.n
    output_file = os.path.join(output_dir, f"groups_{n}.csv")

    # construct CSV header
    header = ["group", "isom"]
    # check first group to decide if we should include perm_isom
    if groups[0].perm_isom:
        header.append("perm_isom")
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
            if "perm_isom" in header:
                row.append(g.perm_isom)
            for galois in g.galois:
                row.extend(galois.nums[key] for key in galois_keys)
            w.writerow(row)
