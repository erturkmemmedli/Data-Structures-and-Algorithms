from collections import deque

def max_sliding_window(A, m):
    Window = deque()
    result = []
    i = 0
    while i < len(A):
        if i == 0:
            Window.append((A[i], i))
            i += 1
            continue           
        if len(Window) != 0 and Window[-1][0] <= A[i]:
            Window.pop()
            continue
        Window.append((A[i], i))
        if i - Window[0][1] > m - 1:
            Window.popleft()
        if i >= m - 1:
            result.append(Window[0][0])  
        i += 1        
    return result
        
if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    assert n == len(A)
    m = int(input())
    assert 1 <= m <= n
    result  = max_sliding_window(A, m)
    print(*result)