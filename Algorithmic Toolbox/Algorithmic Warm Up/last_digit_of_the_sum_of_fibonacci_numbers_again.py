def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18
    F = [0,1]
    sums = [0,1]
    for i in range(2,to_index+1):
        F.append((F[i-1]+F[i-2]) % 10)
        sums.append((F[i]+sums[i-1]) % 10)
        if sums[i-1] == 0 and sums[i] == 1:
            sums = sums[:-2]
            break
    if from_index == 0:
        return abs(sums[to_index % len(sums)])
    else:
        if (from_index % len(sums)) <= (to_index % len(sums)):
            a = sums[to_index % len(sums)] - sums[(from_index - 1) % len(sums)]
            if a >= 0:
                return a
            else:
                return a + 10
        else:
            b = ((sums[-1] - sums[(from_index-1) % len(sums)]) + sums[to_index % len(sums)]) % 10
            if b >= 0:
                return b
            else:
                return b + 10

if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))