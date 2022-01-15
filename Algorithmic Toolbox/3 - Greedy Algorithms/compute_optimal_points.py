def compute_optimal_points(segments):
    position = []
    segments = sorted(segments)
    for i in range(len(segments)):
        if len(position) == 0:
            position.append(segments[i][1])
        if segments[i][1] < position[-1]:
            position = position[:-1]
        if len(position) != 0 and position[-1] >= segments[i][0]:
            continue
        position.append(segments[i][1])
    return position

if __name__ == '__main__':
    n = int(input())
    assert n >= 2
    input_segments = []
    for i in range(n):
        inputs = tuple(map(int, input().split()))
        input_segments.append(inputs)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)