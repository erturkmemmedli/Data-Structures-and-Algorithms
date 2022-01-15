def binary_search(keys, query):
    low = 0
    high = len(keys)-1
    mid = int(low + (high - low) / 2)

    while low <= high:
        if query == keys[mid]:
            return mid
        elif query > keys[mid]:
            low = mid + 1
            mid = int(low + (high - low) / 2)
            continue
        elif query < keys[mid]:
            high = mid - 1
            mid = int(low + (high - low) / 2)
            continue
    return -1

if __name__ == '__main__':
    key = int(input())
    input_keys = list(map(int, input().split()))
    query = int(input())
    input_queries = list(map(int, input().split()))
    
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')