print('Chapter 02 - Exercise 08')
print('')

# Strings are immutable, but we can create new ones
# based on them using builtins

def strsort(entered):
    """
        Returns the input sorted by order
        or lowest unicode value character to highest
        `strsort('cba') will be the string abc`
    """
    if entered == '':
        raise ValueError
    return ''.join(sorted(entered))       

if __name__ == '__main__':
   while True:
      try:
        entered = input('Enter your single word: ')
        processed = strsort(entered)
        print(f"Result: {processed}")
      except (ValueError, IndexError) as e:
         print('Goodbye.')
         break
