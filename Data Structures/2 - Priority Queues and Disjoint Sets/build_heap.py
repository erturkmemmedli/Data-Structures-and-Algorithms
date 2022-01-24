def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * (i + 1)

def sift_down(A, i, n, count, swaps):
    min_node = i
    right = right_child(i)
    if right <= n and A[right] < A[min_node]:
        min_node = right
    left = left_child(i)
    if left <= n and A[left] < A[min_node]:
        min_node = left
    if i != min_node:
        count += 1
        swaps.append((i, min_node))
        A[i], A[min_node] = A[min_node], A[i]
        sift_down(A, min_node, n, count, swaps)

def build_heap(A):
    n = len(A) - 1
    count = 0
    swaps = []
    for i in range(n // 2, -1, -1):
        sift_down(A, i, n, count, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()