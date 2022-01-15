def partition3(values): 
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values) 
    if len(values) < 3:
        return False
    total = sum(values)
    n = len(values) - 1
    a = total // 3
    b = total // 3
    c = total // 3
    store = {}
    partition = [0] * (n + 1)  
    result = total % 3 == 0 and subsets(values, n, a, b, c, store, partition)  
    if not result:
        return 0
    else:
        return 1

def subsets(values, n, a, b, c, store, partition):
    if a == 0 and b == 0 and c == 0:
        return True
    if n < 0:
        return False  
    key = (n, a, b, c)   
    if key not in store:
        A = False
        if a - values[n] >= 0:
            partition[n] = 1
            A = subsets(values, n - 1, a - values[n], b, c, store, partition)
        B = False
        if not A and b - values[n] >= 0:
            partition[n] = 2
            B = subsets(values, n - 1, a, b - values[n], c, store, partition)
        C = False
        if not A and not B and c - values[n] >= 0:
            partition[n] = 3
            C = subsets(values, n - 1, a, b, c - values[n], store, partition)
        store[key] = A or B or C   
    return store[key]

if __name__ == '__main__':
    input_n = int(input())
    input_values = list(map(int, input().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))