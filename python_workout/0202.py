print('Chapter 02 - Exercise 04')
print('')

# Input string is collection of words
# rather than a sentence with punctuation

def pig_latin_sentence():
   while True:
      try:
        pl_sentence_in = input('Enter a sentence to be translated: ')
        pl_sentence_out = []

        for wrd in pl_sentence_in.split(' '):
            if wrd[0] in ['a','e','i','o','u']:
                pl_sentence_out.append(f"{wrd}yay")
                continue
            pl_sentence_out.append(f"{wrd[1:]}{wrd[0]}ay")
        
        print(f'The translation of {pl_sentence_in} is: {" ".join(pl_sentence_out)}')
      except (ValueError, IndexError) as e:
         print('Goodbye.')
         break

if __name__ == '__main__':
    pig_latin_sentence()