print('Chapter 05 - Exercise 20')
print('')
print('Count stats of a text file')


def wc(path) -> tuple:
    """
    Returns as tuple:
        - number of words
        - number of lines
        - number of unique words

       Example
        This is a test file.
        It contains 28 words and 20 different words.
        It also contains 165 characters.
        It also contains 11 lines.
        It is also self-referential.
        Wow!
    """

    chars = []
    words = []
    word_count = 0
    counts = {
        'lines': 0,
        'words': 0,
        'characters': 0,
    }

    unique_words =  set()
    with open(thefile) as f:
        for one_line in f:
            counts['lines'] += 1
            counts['characters'] += len(one_line)
            counts['words'] += len(one_line.split())
            unique_words.update(one_line.split())
    counts['unique_words'] = len(unique_words)
    return counts


if __name__ == '__main__':
    thefile = '/workspaces/python-workout/python_workout/supporting_files/wc.txt'
    counts: dict = wc(thefile)

    for key, value in counts.items():
        print(f"{key}:   {value}")
