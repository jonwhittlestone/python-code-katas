print('Chapter 02 - Exercise 01')
print('')
# If word begins with vowel, add "way"
# If word begins with any other letter, move
# first letter to end of word and add 'ay'

# Supports strings containing letters only.

def pig_latin():
   while True:
      try:
        pl_word_in = input('Enter a word to be translated: ')
        pl_word_out = ''
        if pl_word_in == '':
            raise ValueError
        starts_with = pl_word_in[0]
        if starts_with in ['a','e','i','o','u']:
            pl_word_out = f"{pl_word_in}yay"
        pl_word_out = f"{pl_word_in[1:]}{pl_word_in[0]}ay"

        print(f'The translation of {pl_word_in} is: {pl_word_out}')
      except ValueError as e:
         print('Goodbye.')
         break

if __name__ == '__main__':
    pig_latin()