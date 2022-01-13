def partition3(A, l, r):
    pivot = A[l]
    part1 = l
    part2 = l
    for i in range(l + 1, r + 1):
        if A[i] < pivot:
            part1 += 1
            part2 += 1
            A[i], A[part2] = A[part2], A[i]
            A[part2], A[part1] = A[part1], A[part2]
        elif A[i] == pivot:
            part2 += 1
            A[i], A[part2] = A[part2], A[i]
    A[l], A[part1] = A[part1], A[l]
    return part1, part2

def randomized_quick_sort(A, l, r):
    if l >= r:
        return
    k = randint(l, r)
    A[l], A[k] = A[k], A[l]
    (m1, m2) = partition3(A, l, r)
    randomized_quick_sort(A, l, m1 - 1)
    randomized_quick_sort(A, m2 + 1, r)
