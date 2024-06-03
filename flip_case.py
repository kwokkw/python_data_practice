def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    result = ""
    to_swap_lower = to_swap.lower()

    for char in phrase:
        if char.isupper() and char.lower() == to_swap_lower:
            result = result + char.swapcase()
        elif char == to_swap_lower:
            result = result + char.swapcase()
        else:
            result = result + char
    return result

print(flip_case('Aaaahhh', 'A'))

# string.swapcase()
""" NOTE

*** STRING IS IMMUTABLE ***
    - Therefore, initialize an empty string variable to store the result. 

*** How to append a String *** 
    - Use the `+` operator
    - Use the `join()` method

 """