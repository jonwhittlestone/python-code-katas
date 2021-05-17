print("Chapter 03 - Exercise 09")
print("")

# Being dynamic language, means functions
# in Python can operate on a variety
# of different sequences (string, list, tuple)
# since they are based on the same iterable API

# Write a function, firstlast, that takes a sequence (string, list, or tuple)
# and returns the first and last elements of that sequence, in a two-element sequence of the same type.
#
# So firstlast('abc') will return the string ac,
# while firstlast([1,2,3,4]) will return the list [1,4].


def firstlast(seq):
    """
    Returns two slices, first and last
    """
    if seq == "":
        raise ValueError
    return seq[:1], seq[-1:]


if __name__ == "__main__":
    try:
        inputs = [
            "abc",
            ["yellow", "green", "blue"],
            ("to", "be", "or", "not", "to", "be"),
        ]
        for input_seq in inputs:
            first, last = firstlast(input_seq)
            print(f"First Item of {input_seq} : {first}\nLast Item: {last}")
            print("------")
    except (ValueError, IndexError) as e:
        print("Goodbye.")
