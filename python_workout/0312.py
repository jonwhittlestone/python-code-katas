from collections import Counter
print("Chapter 03 - Exercise 12")
print("")

# Exercise specifies using itemgetter
#   Use `Counter()` - https://docs.python.org/3/library/collections.html?#collections.Counter.most_common


def most_repeating_word(seq):    
   """
      For each word, find the letter that appears the most times
      Example: 
         seq = ['this', 'is', 'an', 'elementary', 'test', 'example']
         result = elementary
            * 'this', 'is', 'an' have no repeating letters
            * 'elementary' has the letter 'e' which repeats three times
            * 'exmple' has a repeating letter: 'e' repeats twice
   """
   # We could iterate
   current_word = ''
   current_tally = 0
   word_letter_counts = []
   for i, w in enumerate(seq.split(' ')):
      word_letter_counts.append(Counter(w).most_common(1))
      if Counter(w).most_common(1)[0][1] > current_tally:
         current_word = seq.split(' ')[i]
         current_tally = Counter(w).most_common(1)[0][1]
   
   # Or we could just use `max`
   current_word = max(seq.split(' '), key=most_repeating_letter_count)
   return current_word

def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1] 

if __name__ == "__main__":
   seq = 'hello hello how are you my friend. The envelope is widening for socialising in the public sphere.' 
   seq = 'this is an elementary test example' 
   result = most_repeating_word(seq)
   print(f'Input to most Repeating Word: {seq}')
   print('')
   print(f'Result: {result}')