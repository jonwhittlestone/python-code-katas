# Using the Splat operator to replicate Unix's `sum` function
# that takes in a variable number of arguments


def mysum(*numbers):
    print("mysum with the splat operator:")
    total = 0
    for n in numbers:
        total = +n
    print(f"Summed is {total}")


if __name__ == "__main__":
    # to call the below with an iterable
    # we could use mysum(*[1,2,3])
    mysum(1, 2, 3)
