def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.

    # Remove duplicates
    ages = list(set(ages))

    # Sort the list
    sorted_ages = sorted(ages)

    # Extract the last two elements
    oldest = sorted_ages[-1]
    second_oldest = sorted_ages[-2]

    return (second_oldest, oldest)


print(two_oldest_ages([1, 2, 10, 8]))
print(two_oldest_ages([6, 1, 9, 10, 4]))
print(two_oldest_ages([1, 5, 5, 2]))

""" MISTAKE 

- To fix the function: 
    1. Use `sorted()` instead of `list.sort()`. The `sorted()` function returns a new sorted list. 
    2. Directly work with the sorted list. 

"""


def mistake(ages):
    ages = list(set(ages))
    # `sort()` returns `None`
    # Assigning `None` to a variable
    sorted_ages = ages.sort()
    # `sorted_ages` is `None``
    # Attempting to access the last elements raise error
    oldest = sorted_ages[-1]
    second_oldest = sorted_ages[-2]
    return (second_oldest, oldest)


# print(mistake([1, 2, 10, 8]))
# print(mistake([6, 1, 9, 10, 4]))
# print(mistake([1, 5, 5, 2]))
