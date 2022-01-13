def binary_search(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4

    low = 1
    high = len(keys)
    if query < keys[low-1] or query > keys[high-1]:
        return -1   
    
    while low <= high:
        mid = int(low + (high-low)/2)
        if keys[mid-1] == query:
            return mid-1
        if low == high and keys[mid-1] != query:
            return -1
        elif keys[mid-1] < query:
            low += 1
        else:
            high -= 1
