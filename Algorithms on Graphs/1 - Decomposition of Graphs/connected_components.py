def DFS(adjacency_list):
    global cc
    result = 0
    visited = [False for _ in range(len(adjacency_list))]
    connected_components = [0 for _ in range(len(adjacency_list))]
    for vertex in range(len(adjacency_list)):
        if visited[vertex] == False:
            explore(adjacency_list, vertex, visited, connected_components)
            cc += 1
            result += 1
    return result

def explore(adjacency_list, vertex, visited, connected_components):
    if visited[vertex] == False:
        visited[vertex] = True
        connected_components[vertex] = cc
        for neighbor in adjacency_list[vertex]: 
            if explore(adjacency_list, neighbor, visited, connected_components):
                return 1
    return 0

if __name__ == '__main__':
    vertex, edge = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(edge)]
    adjacency_list = [[] for _ in range(vertex)]
    for a, b in edges:
        adjacency_list[a - 1].append(b - 1)
        adjacency_list[b - 1].append(a - 1)
    global cc
    cc = 1
    print(DFS(adjacency_list))