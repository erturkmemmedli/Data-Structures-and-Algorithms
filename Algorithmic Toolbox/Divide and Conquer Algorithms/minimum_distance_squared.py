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
    k = random.randint(l, r)
    A[l], A[k] = A[k], A[l]
    (m1, m2) = partition3(A, l, r)
    randomized_quick_sort(A, l, m1 - 1)
    randomized_quick_sort(A, m2 + 1, r)

def distance_calculator(first, second):
    return ((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2) ** 0.5

def minimum_left_right(A):
    minimum = float('inf')
    if len(A) == 3:
        if distance_calculator(A[0], A[1]) <= distance_calculator(A[0], A[2]):
            A = A[0:2] + A[1:]
        else:
            A = A[0::2] + A[1:]
    if len(A) == 2:
        minimum = min(minimum, distance_calculator(A[0], A[1]))
        return minimum
    mid = len(A) // 2
    X = minimum_left_right(A[:mid])
    Y = minimum_left_right(A[mid:])
    d = min(X, Y)
    V = final_test(quicksort(filter_mid(A[:mid], int(d))))
    W = final_test(quicksort(filter_mid(A[mid:], int(d))))
    d_mid = min(V, W)
    return min(d, d_mid)

def filter_mid(A, d):
    mid = len(A) // 2
    P = []
    for i in range(len(A)):
        if abs(A[mid][0] - A[i][0]) <= int(d):
            P.append(A[i])
    return P

def quicksort(A):
    if len(A) <= 1:
        return A
    pivot = A[0]
    less = [y for y in A[1:] if y[1] < pivot[1]]
    greater = [y for y in A[1:] if y[1] >= pivot[1]]
    return quicksort(less) + [pivot] + quicksort(greater)

def final_test(A):
    d_prime = float('inf')
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if abs(i - j) < 7:
                d_prime = min(d_prime, distance_calculator(A[i], A[j]))
            else:
                break
    return d_prime

def zero_check(A):
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            return distance_calculator(A[i], A[i + 1])
        
def minimum_distance_squared(points):
    assert 2 <= len(points) <= 10 ** 5
    l = 0
    r = len(points) - 1
    randomized_quick_sort(points, l, r)
    if zero_check(points) == 0:
        return zero_check(points)
    distance = minimum_left_right(points)
    mid_points = filter_mid(points, distance)
    sort_y = quicksort(mid_points)
    mid_distance = final_test(sort_y)
    minimum = min(distance, mid_distance)
    return minimum
