def explore(adjacency_list, start, end, visited):
    if visited[start] == False:
        if start == end:
            return 1
        visited[start] = True 
        for neighbor in adjacency_list[start]:
            if neighbor == end:
                return 1
            if explore(adjacency_list, neighbor, end, visited):
                return 1
    return 0

if __name__ == '__main__':
    vertex, edge = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(edge)]
    start, end = map(int, input().split())
    start, end = start - 1, end - 1
    adjacency_list = [[] for _ in range(vertex)]
    for a, b in edges:
        adjacency_list[a - 1].append(b - 1)
        adjacency_list[b - 1].append(a - 1)
    visited = [False for _ in range(len(adjacency_list))]
    print(explore(adjacency_list, start, end, visited))
