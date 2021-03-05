# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

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
            check.append(F[i] % m)
    return check[n % len(check)]


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
