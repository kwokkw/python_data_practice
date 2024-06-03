def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_lst = []
    for item in lst:
        if bool(item) == True:
            new_lst.append(item)
    return new_lst

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))

# MISTAKE I MDAE: 

# Logical mistake
# Removnig elements from a list while iterating 
def logical_mistake(lst):
    for item in lst:
        if bool(item) == False:
            lst.remove(item)
    return lst

""" 
When removing an element from a list while iterating over it, the indices of the subsequent elements change, causing the loop to skip checking some elements.

Original list: [0, 1, 2, '', [], False, (), None, 'All done']

Iteration 1:
Index: 0
Element: 0 (False)
Action: Remove 0
List now: [1, 2, '', [], False, (), None, 'All done']

Iteration 2:
Index: 1
Element: 2 (True)
Action: Keep
List remains: [1, 2, '', [], False, (), None, 'All done']

Iteration 3:
Index: 2
Element: '' (False)
Action: Remove ''
List now: [1, 2, [], False, (), None, 'All done']

Iteration 4:
Index: 3
Element: False (False)
Action: Remove False
List now: [1, 2, [], (), None, 'All done']

Iteration 5:
Index: 4
Element: None (False)
Action: Remove None
List now: [1, 2, [], (), 'All done']

Final list: [1, 2, [], (), 'All done']

 """

