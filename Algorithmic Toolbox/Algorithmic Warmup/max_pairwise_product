def max_pairwise_product(A):
    assert 2 <= len(A) <= 2 * 10 ** 5
    assert all(0 <= x <= 2 * 10 ** 5 for x in A)
    if len(A) == 2:
        return A[0] * A[1]
    max1 = 0
    max2 = 0
    for i in range(len(A)):
        if A[i] > max1:
            max2 = max1
            max1 = A[i]
        elif A[i] > max2:
            max2 = A[i]
    return max1 * max2
