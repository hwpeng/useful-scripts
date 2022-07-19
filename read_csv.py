# read csv
import csv
def read_csv(csv_name, verbose=False):
    with open(csv_name) as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        if verbose:
            print(header)
        rows = []
        for row in reader:
            rows.append(row)

    x = []
    for row in rows:
        x.append(row[2][1:])
    if verbose:
        print(x)
    return rows, x
