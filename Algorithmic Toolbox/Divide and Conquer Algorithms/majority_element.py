def majority_element(elements):
    assert 1 <= len(elements) <= 10 ** 5
    l = 0
    r = len(elements) - 1
    randomized_quick_sort(elements, l, r)
    n = len(elements)
    for i in range(0, (n+1)//2):
        if elements[i] == elements[i + n//2]:
            return 1
    return 0
