def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = {"a", "e", "i", "o", "u"}
    chars = [char for char in s if char in vowels]
    chars.reverse()

    # Reconstruct
    result = []
    index = 0
    for char in s:
        if char in vowels:
            result.append(chars[index])
            index += 1
        else:
            result.append(char)
    return result


print(reverse_vowels("Hello!"))

""" NOTE 

Understanding the problem: 

- Identify vowels 
- Reversing the order of vowels
- Preserve non-vowel positions
- Reconstruct the string

 """
