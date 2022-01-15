def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d
    position = 0
    refill = []
    i = 0
    while i < len(stops):
        if stops[0] > m or d - stops[-1] > m or (i > 0 and stops[i] - stops[i - 1] > m):
            return -1
        if stops[i] - position < m:
            i += 1
            continue
        if stops[i] - position == m:
            position = stops[i]
            refill.append(position)
            i += 1
            continue
        if stops[i] - position > m:
            position = stops[i-1]
            refill.append(position)
    if d - position <= m:
        return len(refill)
    else:
        refill.append(stops[-1])
        return len(refill)

if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n
    print(compute_min_number_of_refills(input_d, input_m, input_stops))