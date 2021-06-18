import string
print('Chapter 07 - Exercise 35b')
print('Find Gematria -  match other words with same Gematria score')

GEMATRIA = {char: index
            for index, char in enumerate(string.ascii_lowercase, 1)}


def gematria_for(word: str) -> list:
    chr_exceptions = ['-', '\n']
    score = sum([GEMATRIA[ltr]
                for ltr in word.lower()
                if ltr not in chr_exceptions
                 ])
    return score


def gematria_equal_words(score: int) -> list:

    thefile = '/workspaces/python-workout/python_workout/supporting_files/words.txt'
    return [word.replace('\n', '')
            for word in open(thefile)
            if gematria_for(word) == score]


if __name__ == '__main__':
    try:
        word_in = input(
            'Enter a word, and I will return words of same Grematria score: ')
        if word_in == '':
            raise ValueError
        score: int = gematria_for(word_in)
        res: list = gematria_equal_words(score)
        print(
            f"Other words from file with the same Gematria score as {word_in}:")
        print(res)
    except ValueError as e:
        print('Goodbye')
