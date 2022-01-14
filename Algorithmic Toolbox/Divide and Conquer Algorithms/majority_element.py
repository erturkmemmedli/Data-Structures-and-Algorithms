def majority_element(elements):
    assert 1 <= len(elements) <= 10 ** 5
    elements.sort()
    n = len(elements)
    for i in range(0, (n+1)//2):
        if elements[i] == elements[i + n//2]:
            return 1
    return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))