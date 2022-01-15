def largest_number(numbers):
    assert all(1 <= int(a) <= 10 ** 4 for a in numbers)
    assert 1 <= len(numbers) <= 100
    numbers = list(map(str, numbers))
    i = 1
    while i <= len(numbers) - 1:
        j = i
        while j >= 1:
            if int(numbers[j-1] + numbers[j]) < int(numbers[j] + numbers[j-1]):
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
                j -= 1
            else:
                break
        i += 1
    return int(''.join(map(str, numbers)))

if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))