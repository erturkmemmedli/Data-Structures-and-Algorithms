def points_cover(starts, ends, points):
    assert len(starts) == len(ends)
    pair = []
    for i in range(len(starts)):
        if starts[i] <= ends[i]:
            pair.append((starts[i], 'left'))
            pair.append((ends[i], 'right'))
        else:
            pair.append((ends[i], 'left'))     
            pair.append((starts[i], 'right'))
    for j in range(len(points)):
        pair.append((points[j], 'point'))
    pair.sort()
    result_dictionary = {}
    count_left = 0
    count_right = 0
    for k in pair:
        if k[1] == 'left':
            count_left += 1
        elif k[1] == 'right':
            count_right += 1
        else:
            result_dictionary[f'point {k[0]}'] = count_left - count_right
    # print(result_dictionary)
    final_result = []
    for z in points:
        final_result.append(result_dictionary[f'point {z}'])
    return final_result
