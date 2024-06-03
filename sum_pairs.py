def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    nums_set = set()
    for n in nums:
        difference = goal - n
        if difference in nums_set:
            return (n, difference)
        nums_set.add(n)
    return ()


print(sum_pairs([1, 2, 2, 10], 4))
print(sum_pairs([4, 2, 10, 5, 1], 6))
print(sum_pairs([5, 1, 4, 8, 3, 2], 7))
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))

""" MISTAKE 

The function below does not correctly identify the first pair.

The code consider the current number as part of the pair.
"""


def mistake_sum_pairs(nums, goal):
    nums_set = set({})
    for n in nums:
        nums_set.add(n)  # Add current number to the set
        difference = goal - n
        if difference in nums_set:  # Check if the pair exists
            return (n, difference)
    return ()


print(mistake_sum_pairs([5, 1, 4, 8, 3, 2], 10))  # (5, 5)

""" 
The goal is 10 and the current number is 2. 
The set already contain 5 when the code checks `difference` (which is 5) is in the set. 
This falsely indicate a pair is found. 
 """
