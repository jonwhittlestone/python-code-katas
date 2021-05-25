print('Chapter 04 - Exercise 17')
print('')


def unique_numbers(seq: list):
    return len(set(seq))


if __name__ == '__main__':
    seq = [3, 4, 3, 2, 2, 1, 11, 11, 11]
    print('Count of unique numbers: ')
    print(unique_numbers(seq))
