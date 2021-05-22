import pprint
import operator
from typing import Tuple
print("Chapter 03 - Exercise 13")
print("Printing Tuple Records")
print("")

def format_sort_records(people: list):    
   """
      Displaying formatted records in a table

      Example input
      PEOPLE = [
         ('Donald', 'Trump', 7.85),          
         ('Vladimir', 'Putin', 3.626),          
         ('Jinping', 'Xi', 10.603)
      ]

      Example output
      Trump      Donald      7.85
      Putin      Vladimir    3.63
      Xi         Jinping    10.60
   """
   output = []
   template = "{1:10} {0:10} {2:5.2f}"
   for person in sorted(people, key=operator.itemgetter(1,0)):
      # person = ('Vladimir', 'Putin', '3.626')
      formatted = template.format(*person)
      # formatted = 'Putin      Vladimir    3.63'
      output.append(formatted)
   return '\n'.join(output)

if __name__ == "__main__":
   people = [
      ('Donald', 'Trump', 7.85),          
      ('Vladimir', 'Putin', 3.626),          
      ('Jinping', 'Xi', 10.603)
   ]
   result = format_sort_records(people)
   print('Input People:')
   pprint.pprint(people)
   print('')
   print('Output formatted:')
   print(result)