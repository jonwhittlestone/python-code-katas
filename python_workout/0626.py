print('Chapter 06 - Exercise 26')
print('')
print('Prefix notation calculator - Pythonic switch')


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


def mod(x, y):
    return x % y


def pow(x, y):
    return x**y


operators = {
    "+": add,
    "-": subtract,
    "/": divide,
    "%": mod,
    "**": pow,
}


def calc(exp="+ 3 2"):
    operator, op1, op2 = exp.split(" ")
    return operators[operator](float(op1), float(op2))


if __name__ == '__main__':
    prefix_notation = "+ 3 2"
    res = calc(prefix_notation)

    prefix_notation = "** 12 2"
    res = calc(prefix_notation)

    print(f"Result of {prefix_notation}:\n{res}")
