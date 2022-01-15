def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    counts = [0] * (n + 1)
    if n == 1:
        return [1]
    for i in range(2, n + 1):
        result1 = counts[i - 1] + 1
        if i % 2 == 0:
            result2 = counts[i // 2] + 1
        else:
            result2 = float('inf')
        if i % 3 == 0:
            result3 = counts[i // 3] + 1
        else:
            result3 = float('inf')
        counts[i] = min(result1, result2, result3)
        
    output = [n]
    k = n
    while True:
        if counts[k] == counts[k - 1] + 1:
            k = k - 1
            output.insert(0, k)
        elif k % 2 == 0 and counts[k] == counts[k // 2] + 1:
            k = k // 2
            output.insert(0, k)
        elif k % 3 == 0 and counts[k] == counts[k // 3] + 1:
            k = k // 3
            output.insert(0, k) 
        if k == 1:
            break
    return output

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)