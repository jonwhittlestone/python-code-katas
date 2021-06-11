print('Chapter 07 - Exercise 29')
print('')
print('')

# map and filter
# They exist for historical reasons
# A list comprension is mostly used instead
# but `map` and `filter` ofter are a more terser/simpler
# syntax
# `map` runs a function over each element of an iterable (or multiple)
#   import operator
#   letters = 'abcd'
#   numbers = range(1,5)
#   x = map(operator.mul, letters, numbers)
#   print(' '.join(x))
#   >>> a bb ccc dddd
#
# Equivalent to:
# print(' '.join(operator.mul(one_letter, one_number)
#               for one_letter, one_number in zip(letters, numbers)))

# `filter` pssses a function to filter (treats functions as data)
# where the function evaluates to True or False
# which determines if the element is in the output sequence


def sum_numbers(numbers: str) -> int:
    '''Take a sequence of strings, turn them into numbers
    and then sum them

        Example:
            numbers = '10 abc 20 de44 30 55fg 40'
            Return 100
    '''
    return sum(int(number)
               for number in numbers.split()
               if number.isdigit())


if __name__ == '__main__':
    seq = '10 abc 20 de44 30 55fg 40'
    res = sum_numbers(seq)
    print(f"Sequence: {seq}")
    print(f"Res: {res}")
