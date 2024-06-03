def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

    >>> three_odd_numbers([1, 2, 3, 4, 5])
    True

    >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
    True

    >>> three_odd_numbers([5, 2, 1])
    False

    >>> three_odd_numbers([1, 2, 3, 3, 2])
    False
    """
    for i in range(len(nums) - 2):
        triplets = [nums[i], nums[i + 1], nums[i + 2]]
        if sum(triplets) % 2 != 0:
            return True
    return False


print(three_odd_numbers([1, 2, 3, 4, 5]))
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))
print(three_odd_numbers([5, 2, 1]))
print(three_odd_numbers([1, 2, 3, 3, 2]))

""" NOTE 

Understanding the problem:

The function needs to check whether the sum of any three sequential numbers in the list is odd. 

    - Sequential Numbers: This means every possible set of three numbers that are next to each other in the list.

    - Odd number is any integer that is not divisible by 2.

Example 1: `[1, 2, 3, 4, 5]`

    - Sequential triplets: (1, 2, 3), (2, 3, 4), (3, 4, 5)

 """
