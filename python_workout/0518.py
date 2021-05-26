print('Chapter 05 - Exercise 18')
print('')
print('Reading a file. and returning the final line.')


def get_final_line(thefile: str) -> str:
    with open(thefile) as f:
        contents = f.read()
        lines = contents.split("\n")

    return lines[-1]


if __name__ == '__main__':
    thefile = '/workspaces/python-workout/python_workout/supporting_files/fun.txt'
    final_line = get_final_line(thefile)
    print(final_line)
