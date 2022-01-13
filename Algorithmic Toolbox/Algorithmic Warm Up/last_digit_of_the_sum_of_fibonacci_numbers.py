def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    F = [0,1]
    sums = [0,1]
    for i in range(2,n+1):
        F.append((F[i-1]+F[i-2]) % 10)
        sums.append((F[i]+sums[i-1]) % 10)
        if sums[i-1] == 0 and sums[i] == 1:
            sums = sums[:-2]
            break
    return sums[n % len(sums)]
