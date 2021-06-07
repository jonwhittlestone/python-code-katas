import os
import pathlib
import csv
print('Chapter 05 - Exercise 24')
print('')
print('Reverse Lines')


def reverse_file(path_in: str, path_out):
    """Reverses lines of input file to new output file
    Example input:
        abc def
        ghi jkl
    Example output:
        fed cba
        lkj ihg
    Args:
        path_in (str): The file location of the input file
        path_out (str): The file location of the created output file

    Returns:
        list: a list of strings representing the header columns
    """
    p = pathlib.Path(path_in)
    contents_lines = p.read_text().split('\n')
    with open(path_out, 'w') as f:
        for ln in contents_lines:
            f.write(f"{ln[::-1]}\n")


if __name__ == '__main__':
    output = ''
    IN_FILE = os.path.join('.', 'python_workout',
                       'supporting_files', '0524_reverselines','0524_reverse_lines.txt')
    OUT_FILE = os.path.join('.', 'python_workout',
                       'supporting_files', '0524_reverselines','0524_OUTPUT_reverselines.txt')
    reverse_file(IN_FILE, OUT_FILE)
    print(f'Written to: {OUT_FILE} ')
