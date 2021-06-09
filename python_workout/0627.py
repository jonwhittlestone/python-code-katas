import random
print('Chapter 06 - Exercise 27')
print('Password Generator - inner functions/"closures"')


def create_password_generator(characters: str):
    """A factory for password generation functions
        using the same set of characters in in_pass.

    Args:
        characters (str): the pwd must contain these chars

    Returns:
        func: create_password(length: int)
    """
    def create_password(length: int):
        output = []
        for i in range(length):
            output.append(random.choice(characters))
        return ''.join(output)
    return create_password


if __name__ == '__main__':
    """
        Examples:
                Examples should be written in doctest format, and should illustrate how
                to use the function.
        >>> alpha_password = create_password_generator('abcdef')
        >>> symbol_password = create_password_generator('!@#$%')
        >>> print(alpha_password(5))
        efeaa
        >>> print(alpha_password(10))
        cacdacbada
        >>> print(symbol_password(5))
        %#@%@
    """
    in_characters = 'abcdef'
    alpha_password = create_password_generator(in_characters)
    print(
        f"From input:\t{in_characters}, characters\nResult:\t{alpha_password(5)}")
