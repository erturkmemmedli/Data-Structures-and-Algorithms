def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d
    position = 0
    refill = []
    i = 0
    while i <= len(stops) - 1:
        if stops[i] - position < m:
            i += 1
            continue
        if stops[i] - position == m:
            position = stops[i]
            refill.append(position)
            i += 1
            continue
        if (stops[i] - position > m):
            if stops[i] - stops[i-1] <= m:
                position = stops[i-1]
                refill.append(position)
            else:
                return -1 # "Impossible"
    if d - position <= m:
        return len(refill)
    else:
        refill.append(stops[-1])
        return len(refill)
