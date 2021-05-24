import pprint
#
# print(dictdiff(d1, d1))
# >> {}

# print(dictdiff(d1, d2))
# >> {'c': [3, 4]}

# d3 = {'a':1, 'b':2, 'd':3}
# d4 = {'a':1, 'b':2, 'c':4}
# print(dictdiff(d3, d4))
# >> {'c': [None, 4], 'd': [3, None]}

# d5 = {'a':1, 'b':2, 'd':4}
# print(dictdiff(d1, d5))
# >> {'c': [3, None], 'd': [None, 4]}


def dictdiff(first: dict, second: dict) -> dict:
    """
        Returns a new dict that expresses the 
        difference between the two dicts.
        
        For each key-value pair that differs, the return value of dictdiff will have a key-value pair in 
        which the value is a list containing the values 
        from the two different dicts
        
        If one of the dicts doesn’t contain that key, it should contain None
    """
    output = {}    
    all_keys = first.keys() | second.keys()
    for key in all_keys:        
        if first.get(key) != second.get(key):            
            output[key] = [
                first.get(key),                           
                second.get(key)]
    return output


if __name__ == "__main__":
    print('Example 1')
    diff = dictdiff(
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 1, 'b': 2, 'c': 4},
    )
    pprint.pprint(diff)
    print('')
    # ---
    print('Example 2')
    d3 = {'a': 1, 'b': 2, 'd': 3}
    d4 = {'a': 1, 'b': 2, 'c': 4}
    diff = dictdiff(d3, d4)
    pprint.pprint(diff)
    print('')
    # ---
    print('Example 3')
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d5 = {'a': 1, 'b': 2, 'd': 4}
    diff = dictdiff(d1, d5)
    pprint.pprint(diff)
