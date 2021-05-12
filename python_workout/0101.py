import random
print('Chapter 01 - Exercise 01')
print('Number Guessing Game')

LOWER_BOUND = 10
UPPER_BOUND = 30

def guessing_game():
    name = input('Enter your name: ')
    print(f"Ready {name} .....?\n")
    num_to_guess = random.randint(LOWER_BOUND,UPPER_BOUND)
    in_num_to_guess = int(input(f'Guess a number between {LOWER_BOUND} and {UPPER_BOUND}: '))
    while num_to_guess != in_num_to_guess:
        if in_num_to_guess < num_to_guess:
            print('Too Low!')

        if in_num_to_guess > num_to_guess:
            print('Too High!')

        in_num_to_guess = int(input(f'Guess again (between {LOWER_BOUND} and {UPPER_BOUND} ): '))

    print(f'Congratulations! You correctly guessed {num_to_guess}')
    


if __name__ == '__main__':
    guessing_game()