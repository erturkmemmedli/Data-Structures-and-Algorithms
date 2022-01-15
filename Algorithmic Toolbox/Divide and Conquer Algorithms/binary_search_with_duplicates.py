def binary_search_with_duplicates(keys, query):
    low = 0
    high = len(keys)-1
    mid = int(low + (high - low) / 2)
    if query in dictionary:
        return dictionary[query]
    while low <= high:
        if query == keys[mid]:
            while mid > -1 and query == keys[mid]:
                if mid != 0 and keys[mid//2] == keys[mid]:
                    mid = mid // 2
                else:
                    mid -= 1
            mid += 1
            dictionary[query] = mid
            return mid
        elif query > keys[mid]:
            low = mid + 1
            mid = int(low + (high - low) / 2)
        elif query < keys[mid]:
            high = mid - 1
            mid = int(low + (high - low) / 2)
    return -1

if __name__ == '__main__':
    global dictionary
    dictionary = {}
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys
    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries
    for q in input_queries:
        print(binary_search_with_duplicates(input_keys, q), end=' ')