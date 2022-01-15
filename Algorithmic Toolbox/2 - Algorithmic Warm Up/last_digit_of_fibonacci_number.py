def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    F = [0,1]
    for i in range(2,n+1):
        F.append((F[i-1]+F[i-2]) % 10)
        if F[i-1] == 0 and F[i] == 1:
            F = F[:-2]
            break
    return F[n % len(F)]

if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))