def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)
    n = len(weights)
    A = [[0] * (capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            A[i][j] = A[i][j-1]
            if j >= weights[i-1]:
                A[i][j] = weights[i-1] + A[i-1][j - weights[i-1]]
            if A[i][j] < A[i-1][j]:
                A[i][j] = A[i-1][j]
    return A[n][capacity]

if __name__ == '__main__':
    input_capacity, n = list(map(int, input().split()))
    input_weights = list(map(int, input().split()))
    assert len(input_weights) == n
    print(maximum_gold(input_capacity, input_weights))