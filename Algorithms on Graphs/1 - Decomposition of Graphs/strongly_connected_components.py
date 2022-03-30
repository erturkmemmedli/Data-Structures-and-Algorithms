import sys
sys.setrecursionlimit(200000)

def DFS(adjacency_list, adjacency_list_reversed):
    global scc
    result = 0
    visited = [False for _ in range(len(adjacency_list))]
    postorder = []
    strongly_connected_components = [0 for _ in range(len(adjacency_list))]
    for vertex in range(len(adjacency_list)):
        if visited[vertex] == False:
            explore(adjacency_list_reversed, vertex, visited, postorder, strongly_connected_components)
    postorder_reversed = postorder[::-1]
    visited = [False for _ in range(len(adjacency_list))]
    postorder = []
    strongly_connected_components = [0 for _ in range(len(adjacency_list))]
    for vertex in postorder_reversed:
        if visited[vertex] == False:
            explore(adjacency_list, vertex, visited, postorder, strongly_connected_components)
            scc += 1
            result += 1
    #print('strongly connected components:', strongly_connected_components)
    return result

def explore(adjacency_list, vertex, visited, postorder, strongly_connected_components):
    visited[vertex] = True
    strongly_connected_components[vertex] = scc
    for neighbor in adjacency_list[vertex]:
        if visited[neighbor] == False:
            explore(adjacency_list, neighbor, visited, postorder, strongly_connected_components)
    postorder.append(vertex)

if __name__ == '__main__':
    vertex, edge = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(edge)]
    adjacency_list = [[] for _ in range(vertex)]
    adjacency_list_reversed = [[] for _ in range(vertex)]
    for a, b in edges:
        adjacency_list[a - 1].append(b - 1)
        adjacency_list_reversed[b - 1].append(a - 1)
    global scc
    scc = 1
    print(DFS(adjacency_list, adjacency_list_reversed))