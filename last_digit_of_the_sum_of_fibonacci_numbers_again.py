# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(n, m):
    assert 0 <= n <= m <= 10 ** 18

    if m == 0:
        return 0

    F = [0,1]
    check = [0,1]
    for i in range(2,m+1):
        F.append((F[i-1] + F[i-2]))
        if (i-2) != 0 and check[i-2:i] == [0,1]:
            check = check[:-2]
            break
        else:
            check.append(F[i] % 10)
    if n % len(check) <= m % len(check):
        return sum(check[n % len(check) : m % len(check) + 1]) % 10
    else:
        return (sum(check[n % len(check) : ]) + sum(check[ : m % len(check) + 1])) % 10

if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
