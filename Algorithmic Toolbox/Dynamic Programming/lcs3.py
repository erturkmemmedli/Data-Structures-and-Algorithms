def matrix_3D(x, y, z):
    n = len(x)
    m = len(y)
    k = len(z)

    A = [[[0] * (k+1) for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, k+1):
                v1 = A[i][j][k-1]
                v2 = A[i][j-1][k]
                v3 = A[i][j-1][k-1]
                v4 = A[i-1][j][k]
                v5 = A[i-1][j][k-1]
                v6 = A[i-1][j-1][k]
                v7 = A[i-1][j-1][k-1]
                match = A[i-1][j-1][k-1] + 1

                if x[i-1] == y[j-1] == z[k-1] and v1 == v2 == v3 == v4 == v5 == v6 == v7:
                        A[i][j][k] = max(v1, v2, v3, v4, v5, v6, match)
                else:
                    A[i][j][k] = max(v1, v2, v3, v4, v5, v6, v7)  
    return A

def backtracking(result, first_sequence, second_sequence, third_sequence, A, i, j, k):
    if i == 0 or j == 0 or k == 0:
        return
    if i > 0 and j > 0 and k > 0 and A[i][j][k] == A[i][j][k-1]:
        backtracking(result, first_sequence, second_sequence, third_sequence, A, i, j, k-1)
    elif i > 0 and j > 0 and k > 0 and A[i][j][k] == A[i][j-1][k]:
        backtracking(result, first_sequence, second_sequence, third_sequence, A, i, j-1, k)
    elif i > 0 and j > 0 and k > 0 and A[i][j][k] == A[i-1][j][k]:
        backtracking(result, first_sequence, second_sequence, third_sequence, A, i-1, j, k)
    else:
        backtracking(result, first_sequence, second_sequence, third_sequence, A, i-1, j-1, k-1)
        result.append(first_sequence[i-1])

def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100
    
    matrix = matrix_3D(first_sequence, second_sequence, third_sequence)
    i = len(matrix) - 1
    j = len(matrix[0]) - 1
    k = len(matrix[0][0]) - 1
    result = []
    backtracking(result, first_sequence, second_sequence, third_sequence, matrix, i, j, k)
    return len(result)
