def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    current_num = 1
    for n in nums:
        if n % 2 == 0:
            current_num = current_num * n
    return 1 if current_num == 1 else current_num
        
print(multiply_even_numbers([1, 3, 5]))