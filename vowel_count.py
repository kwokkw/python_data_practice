def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase_lower = phrase.lower()
    vowels = "aeiou"
    vowel_count = {}

    for char in phrase_lower:
        if char in vowels:
            vowel_count[char] = vowel_count.get(char, 0) + 1

    return vowel_count

print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))

""" get(self, key, default=None, /)
    Return the value for key if key is in the dictionary, else default.
 
For 'o':
    vowel_count.get('o', 0) returns 0.
    vowel_count['o'] = 0 + 1 → vowel_count = {'o': 1}

For 'o' (second occurrence):
    vowel_count.get('o', 0) returns 1 (current count).
    vowel_count['o'] = 1 + 1 → vowel_count = {'o': 2}
 
 """