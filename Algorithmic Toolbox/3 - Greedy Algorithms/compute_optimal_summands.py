def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    i = 1
    while n > 0:
        if len(summands) == 0:
            summands.append(i)
        n -= i
        if n > summands[-1]:
            i += 1
            summands.append(i)
        else:
            summands[-1] += n
            break
    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)