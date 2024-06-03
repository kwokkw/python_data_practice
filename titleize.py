def titleize(phrase):
    """Return phrase in title case (each word capitalized).

    >>> titleize('this is awesome')
    'This Is Awesome'

    >>> titleize('oNLy cAPITALIZe fIRSt')
    'Only Capitalize First'
    """
    phrase_lst = phrase.split()
    capitalized_words = [w.capitalize() for w in phrase_lst]
    titleized_words = " ".join(capitalized_words)
    return titleized_words


print(titleize("this is awesome"))
