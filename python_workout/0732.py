print('Chapter 07 - Exercise 32')
print('Reversing a dict, with a dictionary comprehension')
print('')

if __name__ == '__main__':
    d = {'a': 1, 'b': 2, 'c': 3}
    print({v: k for k, v in d.items()})
