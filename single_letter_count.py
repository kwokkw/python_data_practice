def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    lower_w = word.lower()
    lower_l = letter.lower()
    return lower_w.count(lower_l)

print(single_letter_count('Hello World', 'l'))