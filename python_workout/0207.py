print('Chapter 02 - Exercise 07')
print('')

# Ex. 07/50
# Put an 'ub' before every vowel sound
# Eg. 'milk' -> 'mubilk' ("moo-bilk")
# Eg. 'program' -> 'pruboogrubam' 
# Ignore capital letters, punctuation, corner cases
# When you have two vowels next to one another -> 'ub' preface
# examples
# 'octopus'     -> 'uboct ubo pubus
# 'elephant'    -> 'ubel ubeph ubant

def ubbi_dubbi(entered):
    processed = []
    if entered == '':
        raise ValueError
    for ltr in entered:
        if ltr in ['a','e','i','o','u']:
            processed.append('u')
            processed.append('b')
            processed.append(ltr)
        else:
            processed.append(ltr)
    return ''.join(processed)       

if __name__ == '__main__':
   while True:
      try:
        entered = input('Enter your single word: ')
        processed = ubbi_dubbi(entered)
        print(f"Translation: {processed}")
      except (ValueError, IndexError) as e:
         print('Goodbye.')
         break