def merge_sort(A):
    if len(A) == 1:
        return A
    mid = len(A) // 2
    B = merge_sort(A[:mid])
    C = merge_sort(A[mid:])
    A_new = merge(B, C)
    return A_new

def merge(B, C):
    global count
    D = []
    while len(B) != 0 and len(C) != 0:
        b = B[0]
        c = C[0]
        if b <= c:
            D.append(b)
            B = B[1:]
        else:
            count += len(B)
            D.append(c)
            C = C[1:]
    D = D + B + C
    return D

def compute_inversions(a):
    assert len(a) <= 300000
    global count
    count = 0
    merge_sort(a)
    return count

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))