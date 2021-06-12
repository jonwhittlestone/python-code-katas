print('Chapter 07 - Exercise 31')
print('Pig Latin file')
print('')


def move_punctuation_ending(word) -> str:
    letters = []
    ending = ''
    for ltr in word:
        if ltr in [',', '!', '.']:
            ending = ltr
        else:
            letters.append(ltr)
    letters.append(ending)
    return ''.join(letters)


def pl_word(word, word_position='', sentence_length=''):
    starts_with = word[0]
    if starts_with in ['a', 'e', 'i', 'o', 'u']:
        translated = f"{word}yay"
    translated = f"{word[1:]}{word[0]}ay"
    return move_punctuation_ending(translated)


def pl_line(line: list) -> str:
    return ' '.join(line)


def pig_latin_file(path: str):
    """First, transforms each word of a line to pig latin
    Then prints them to string"""

    ret = []
    line_words = []
    with open(path) as f:
        for one_line in f:
            line_words.append([pl_word(w)
                              for w in one_line.split()])

    ret = [
        pl_line(line)
        for line in line_words
        if len(line) > 0
    ]

    return "\n".join(ret)


if __name__ == '__main__':
    """Proposed solution uses nested list comp:


        def plword(word):
            if word[0] in 'aeiou':
                return word + 'way'

            return word[1:] + word[0] + 'ay'


        def plfile(filename):
            return ' '.join(plword(one_word)
                            for one_line in open(filename)        ❶
                            for one_word in one_line.split())    ❷
    """
    thefile = '/workspaces/python-workout/python_workout/supporting_files/wc.txt'
    print(pig_latin_file(thefile))
