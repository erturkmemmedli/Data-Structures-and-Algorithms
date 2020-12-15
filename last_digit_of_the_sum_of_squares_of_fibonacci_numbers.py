# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

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

    return check[n % len(check)] * (check[n % len(check)] + check[n % len(check)-1]) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
