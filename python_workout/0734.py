print('Chapter 07 - Exercise 34')
print('Identify supervocalic words with set comprehensions')
print('')


def get_sv(path: str):
    """Check whether items from list are
    in a word with the < operator.
        We iterate over the lines of the file.              
        We turn each word into a set and check that the vowels are a subset of our word’s letters.              
        If the word passes this test, we include it (the word) in the output.              
        The output is all put into a set, thanks to a set comprehension.
    """

    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {word.strip()
            for word in open(path)
            if vowels < set(word.lower())}


if __name__ == '__main__':
    """Identify supervocalic words with set comprehensions
    Supervocalic words definition: words that contain all vowels (any order)
    """

    thefile = '/workspaces/python-workout/python_workout/supporting_files/words.txt'
    res = get_sv(thefile)
    print(f"Supervocalic words found in file: ")
    print(res)
