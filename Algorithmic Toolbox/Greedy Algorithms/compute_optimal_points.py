def compute_optimal_points(segments):
    position = []
    segments = sorted(segments)
    for i in range(len(segments)):
        if len(position) == 0:
            position.append(segments[i][1])
        if segments[i][1] < position[-1]:
            position = position[:-1]
        if position[-1] >= segments[i][0]:
            continue
        position.append(segments[i][1])
    print(position)
    return len(position)
