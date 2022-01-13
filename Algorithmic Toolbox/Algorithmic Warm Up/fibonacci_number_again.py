def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 6
    F = [0,1]
    for i in range(2,n+1):
        F.append((F[i-1]+F[i-2]) % m)
        if F[i-1] == 0 and F[i] == 1:
            F = F[:-2]
            break
    return F[n % len(F)]
