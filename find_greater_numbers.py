def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    counter = 0
    for i in range(len(nums)):
        current_num = nums[i]
        # print("current number: ", current_num)
        for j in range(i + 1, len(nums)):
            next_num = nums[j]
            # print("next number: ", next_num)
            if next_num > current_num:
                counter += 1
    return counter


# print(find_greater_numbers([1, 2, 3]))
print(find_greater_numbers([6, 1, 2, 7]))
# print(find_greater_numbers([5, 4, 3, 2, 1]))
# print(find_greater_numbers([]))


""" NOTE

Return `# of times`, so a `counter` is needed to keep track of it 

Loop through the list.

Compare the numbers.

 """
