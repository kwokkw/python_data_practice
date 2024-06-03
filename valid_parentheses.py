def valid_parentheses(parens):
    """Are the parentheses validly balanced?

    >>> valid_parentheses("()")
    True

    >>> valid_parentheses("()()")
    True

    >>> valid_parentheses("(()())")
    True

    >>> valid_parentheses(")()")
    False

    >>> valid_parentheses("())")
    False

    >>> valid_parentheses("((())")
    False

    >>> valid_parentheses(")()(")
    False
    """
    counter = 0
    if parens.startswith(")"):
        return False
    for p in parens:
        if p == "(":
            counter += 1
        else:
            counter -= 1
    return counter == 0


print(valid_parentheses("()"))
print(valid_parentheses("()()"))
print(valid_parentheses("(()())"))
print(valid_parentheses(")()"))
print(valid_parentheses("())"))
print(valid_parentheses("((())"))
print(valid_parentheses(")()("))

""" NOTE

Problem:

Balance parenthesis -  every opening parenthesis 
'(' has a corresponding closing parenthesis ')'.

Order Matters - parenthesis must be correctly nested. 
"(()())" is valid, but "())(" is not.

Approach to solve the problem:

Initialize a counter to keep track of the balance between 
opening and closing parenthesis. 

    - Increment the counter for every '('
    - Decrement the counter for every ')'

If counter becomes negative, it means there's a closing 
parenthesis without a matching opening parenthesis, and 
vice versa. 

 """
