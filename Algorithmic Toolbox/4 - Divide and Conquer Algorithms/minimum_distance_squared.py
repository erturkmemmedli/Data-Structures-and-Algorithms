from collections import namedtuple
Point = namedtuple('Point', 'x y')

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
    V = final_test(sorted(filter_mid(A[:mid], int(d)), key = lambda x: x[1]))
    W = final_test(sorted(filter_mid(A[mid:], int(d)), key = lambda x: x[1]))
    d_mid = min(V, W)
    return min(d, d_mid)

def filter_mid(A, d):
    mid = len(A) // 2
    P = []
    for i in range(len(A)):
        if abs(A[mid][0] - A[i][0]) <= int(d):
            P.append(A[i])
    return P

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
    points.sort()
    if zero_check(points) == 0:
        return zero_check(points)
    distance = minimum_left_right(points)
    mid_points = filter_mid(points, distance)
    sort_y = sorted(mid_points, key = lambda x: x[1])
    mid_distance = final_test(sort_y)
    minimum = min(distance, mid_distance)
    return minimum

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)
    print("{0:.9f}".format((minimum_distance_squared(input_points))))