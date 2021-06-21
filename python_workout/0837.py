from menu import menu, an_apple_pie, beef_stroganoff
print('Chapter 08 - Exercise 37')
print('Executing functions as key-value pairs from a module')
print('')

if __name__ == '__main__':
    return_value = menu(a=beef_stroganoff,
                        b=an_apple_pie)

    print(return_value)
