def edit_distance(A, B):
    assert type(A) == str and type(B) == str
    assert len(A) <= 100 and len(B) <= 100
    A = A.upper()
    B = B.upper()
    m = len(A)
    n = len(B)
    EditMatrix = [[0] * (n+1) for i in range(m+1)]
    for i in range(1, m+1):
        EditMatrix[i][0] = EditMatrix[i-1][0] + 1
    for i in range(1, n+1):
        EditMatrix[0][i] = EditMatrix[0][i-1] + 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            insertion = EditMatrix[i][j-1] + 1
            deletion = EditMatrix[i-1][j] + 1
            mismatch = EditMatrix[i-1][j-1] + 1
            match = EditMatrix[i-1][j-1]
            if A[i-1] != B[j-1]:
                EditMatrix[i][j] = min(insertion, deletion, mismatch)
            else:
                EditMatrix[i][j] = min(insertion, deletion, match)
    if len(A) == 0:
        return len(B)
    if len(B) == 0:
        return len(A)
    return EditMatrix[i][j]

if __name__ == "__main__":
    print(edit_distance(input(), input()))