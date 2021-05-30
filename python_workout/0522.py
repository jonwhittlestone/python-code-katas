import csv
import os
import pathlib
print('Chapter 05 - Exercise 22')
print('')
print('Reading and writing CSV')


def passwd_to_csv(in_file, out_file):
    p = pathlib.Path(in_file)
    contents_lines = p.read_text().split('\n')
    with open(out_file, 'w') as f:
        o = csv.writer(f, delimiter="\t")
        for ln in contents_lines:
            row = ln.split(':')
            if len(row) > 1:
                o.writerow([row[0], row[2]])

    print(f"Finished writing to {out_file}")


if __name__ == '__main__':
    DIR = os.path.join('.', 'python_workout',
                       'supporting_files')
    in_file = os.path.join(DIR, 'passwd')
    out_file = os.path.join(DIR, 'passwd.csv')

    passwd_to_csv(in_file, out_file)
