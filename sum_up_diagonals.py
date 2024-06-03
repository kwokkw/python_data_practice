def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3], 0, 2
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # Create two variables to keep track of the sums of the two diagonal.
    primary_diagonal = 0
    second_diagonal = 0

    # Outer loop
    for i in range(len(matrix)):
        # Inner loop
        for j in range(len(matrix[i])):
            # Debug purpose
            # print(f"i: {i}, j: {j}")
            # Primary diagonal check
            if i == j:
                primary_diagonal += matrix[i][j]
            # Second diagonal check (see NOTE)
            if i + j == len(matrix) - 1:
                second_diagonal += matrix[i][j]

    return primary_diagonal + second_diagonal


m1 = [
    [1, 2],
    [30, 40],
]
print(sum_up_diagonals(m1))

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(sum_up_diagonals(m2))

""" NOTE
Two main diagonals of a square matrix. 
    - Primary diagonal, top-left to bottom-right.
    - Secondary diagonal, bottom-left to top-right or top-right to bottom left. 

Identify the indices
    - Primary diagonal: (0,0), (1,1), (2,2)
    - Secondary diagonal: (0, 2), (1,1), (2,0)

Primary Diagonal in a Square Matrix: 
  - Check if the row index `i` is equal to the column index `j`.

Secondary Diagonal in a Square Matrix: 
  >>> For `n * n` matrix, the elements on the secondary diagonal have the following pattern in terms of their indices:
        ...  First Element: (0, n - 1)
        ...  Second Element: (0, n - 2)
        ...  Thire Element: (0, n - 3)
        ...  ...
        ...  Last Element: (n -1, 0)

 Index Relationship, For any element on the secondary diagonal, the sum of the row index i and the column index j is always equal to: n - 1
 i + j = n - 1
 """
