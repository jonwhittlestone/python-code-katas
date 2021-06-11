from typing import List
print('Chapter 07 - Exercise 30')
print('')
print('Flatten a nested list - nested list comprehension')


def flatten_it(l: List[list]) -> list:
    return [item
            for sub in l
            for item in sub]


if __name__ == '__main__':
    two_deep_list = [[1, 2], [3, 4], [5, 6]]
    res = flatten_it(two_deep_list)
    print(f"Input: {two_deep_list}")
    print(f"Flattened Result: {res}")
