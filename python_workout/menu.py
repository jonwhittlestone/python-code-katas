def beef_stroganoff():
    return 'Here is: beef stroganoff'


def an_apple_pie():
    return 'Here is: apple pie'


def menu(**options):
    option_string = '/'.join(sorted(options))
    while True:
        choice = input(f'Please make your choice from, {option_string} ')
        if choice in options:
            return options[choice]()
        print(f'{choice} is not an option.')
