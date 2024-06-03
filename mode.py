def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    count = 0
    num_count = {}
    for n in nums:
        if n in num_count:
            num_count[n] += 1
        else:
            num_count[n] = 1

    highest_count = 0
    for (num, count) in num_count.items():
        if count > highest_count:
            highest_count = count
            most_common_num = num
    return most_common_num

print(mode([2, 2, 3, 3, 2, 4, 4, 4, 4, 4, ]))