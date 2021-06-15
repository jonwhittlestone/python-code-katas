print('Chapter 07 - Exercise 33')
print('Transforming a values in a dict')
print('')


def transform_values(func, d: dict):
    return {k: func(v)
            for k, v in d.items()}


if __name__ == '__main__':
    """Transform values in a dict using a 
    lambda/anonymous func"""
    d = {'a': 1, 'b': 2, 'c': 3}
    res: dict = transform_values(lambda x: x*x, d)
    print(f"Input: {d}")
    print(f"Output: {res}")
