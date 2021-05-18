print("Chapter 03 - Exercise 10")
print("")

# Run methods not on the argument
# But on elements within the argument
# Eg. Sum the elements of a list regardless
# of whether elements data type


def mysum(*seq):
    """
    All items should be able
    to respond to the '+' operator
    Accepted:
        numbers, strings, lists and tuples
    Not Accepted:
        sets and dicts
    """
    if not seq:
        raise ValueError
    ret = seq[0]
    for item in seq[1:]:
        ret += item

    return ret


if __name__ == "__main__":
    try:
        result = mysum('abc', 'def')     # expect 'abcdef'
        print(f"Result of `mysum('abc','def')`: {result}")
        result = mysum([1, 2, 3], [4, 5, 6])     # expect [1,2,3,4,5,6]
        print(f"Result of `mysum([1,2,3],[4,5,6])`: {result}")
        print("------")
    except (ValueError, IndexError) as e:
        print("Goodbye.")
