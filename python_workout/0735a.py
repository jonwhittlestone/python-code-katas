import string
print('Chapter 07 - Exercise 35a')
print('Create Gematria -  a map/dict of letters to numbers')


def gematria() -> dict:
    var = 'a'
    return {(chr(ord(var)+i)): i+1
            for i in range(26)}
    # book solution
    # return {char: index
    #        for index, char in enumerate(string.ascii_lowercase, 1)}


if __name__ == '__main__':
    res = gematria()
    print(res)
