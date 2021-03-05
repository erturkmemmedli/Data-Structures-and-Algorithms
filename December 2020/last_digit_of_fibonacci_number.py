# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    F = [0,1]
    check = [0,1]
    for i in range(2,n+1):
        F.append((F[i-1] + F[i-2]))
        if (i-2) != 0 and check[i-2:i] == [0,1]:
            check = check[:-2]
            break
        else:
            check.append(F[i] % 10)
    return check[n % len(check)]



if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
