import pprint
import operator
print("Chapter 03 - Exercise 11")
print("Alphabetising Names")
print("")

# Exercise specifies using itemgetter
#   https://docs.python.org/3/library/operator.html?#operator.itemgetter

PEOPLE = [{'first':'Jon', 'last':'Whittlestone',
    'email':'jwhittlestone@hotmail.com'},
 {'first':'Joe', 'last':'Biden',
    'email':'president@whitehouse.gov'},
 {'first':'Vladimir', 'last':'Putin',
    'email':'president@kremvax.ru'}
 ]

def alphabetize_names(list_of_dicts):    
    return sorted(list_of_dicts,        
                key=operator.itemgetter('last', 'first')) 

if __name__ == "__main__":
    print('Unsorted:')
    pprint.pprint(PEOPLE)

    print('Sorted:')
    sorted_result = alphabetize_names(PEOPLE)
    pprint.pprint(sorted_result)