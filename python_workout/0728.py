print('Chapter 07 - Exercise 28')
print('')
print('')


def join_numbers(range_of_numbers: int):
    return ','.join([str(n)
                    for n in range(15)])


if __name__ == '__main__':
    range_of_numbers = 15
    print(f"Range of Numbers: {range_of_numbers}")
    print(f"Result: {join_numbers(range_of_numbers)}")
