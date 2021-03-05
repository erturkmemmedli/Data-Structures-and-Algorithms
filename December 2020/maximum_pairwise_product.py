# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    index_1 = 0
    for i in range(len(numbers)):
        if ((index_1 == 0) | (numbers[i] > numbers[index_1])):
            index_1 = i
    index_2 = 0
    for j in range(len(numbers)):
        if ((j != index_1) & ((index_1 == 0) | (numbers[j] > numbers[index_2]))):
            index_2 = j
    return numbers[index_1] * numbers[index_2]

def max_pairwise_product_new(a):

    a.sort(reverse=True)
    return a[0]*a[1]


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product_new(input_numbers))
