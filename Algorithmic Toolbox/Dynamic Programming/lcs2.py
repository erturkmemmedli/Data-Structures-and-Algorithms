def matching_matrix(first_sequence, second_sequence):
    n = len(first_sequence)
    m = len(second_sequence)
    A = [[0] * (m+1) for _ in range(n+1)] 
    for i in range(1, n+1):
        A[i][0] = 0
    for i in range(1, m+1):
        A[0][i] = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            left = A[i][j-1]
            top = A[i-1][j]
            diagonal = A[i-1][j-1]
            match = A[i-1][j-1] + 1
            if first_sequence[i-1] == second_sequence[j-1] and left == top == diagonal:
                A[i][j] = max(left, top, match)
            else:
                A[i][j] = max(left, top, diagonal)
    return A

def optimize(result, first_sequence, second_sequence, A, i, j):
    if i == 0 and j == 0:
        return
    if i > 0 and j > 0 and A[i][j] == A[i-1][j] == A[i][j-1] == A[i-1][j-1]:
        optimize(result, first_sequence, second_sequence, A, i-1, j-1)
    elif i > 0 and A[i][j] == A[i-1][j]:
        optimize(result, first_sequence, second_sequence, A, i-1, j)
    elif j > 0 and A[i][j] == A[i][j-1]:
        optimize(result, first_sequence, second_sequence, A, i, j-1)
    else:
        optimize(result, first_sequence, second_sequence, A, i-1, j-1)
        result.append(first_sequence[i-1])

def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100 and len(second_sequence) <= 100 
    matrix = matching_matrix(first_sequence, second_sequence)
    i = len(matrix) - 1
    j = len(matrix[0]) - 1
    result = []
    optimize(result, first_sequence, second_sequence, matrix, i, j)
    return len(result)
