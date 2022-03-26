def DFS(adjacency_list):
    visited = [[False, False] for _ in range(len(adjacency_list))]
    for vertex in range(len(adjacency_list)):
        if visited[vertex][1] == False:
            if visited[vertex][0] == False:
                if explore(adjacency_list, vertex, visited):
                    return 1
    return 0

def explore(adjacency_list, vertex, visited):
    if visited[vertex][1] == False:
        if visited[vertex][0] == False:
            visited[vertex][0] = True
            for neighbor in adjacency_list[vertex]:
                if explore(adjacency_list, neighbor, visited):
                    return 1
                visited[vertex][1] = True
        if len(adjacency_list[vertex]) == 0:
            visited[vertex][1] = True
    if visited[vertex][1] == True:
        return 0
    return 1

if __name__ == '__main__':
    vertex, edge = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(edge)]
    adjacency_list = [[] for _ in range(vertex)]
    for a, b in edges:
        adjacency_list[a - 1].append(b - 1)
    print(DFS(adjacency_list))