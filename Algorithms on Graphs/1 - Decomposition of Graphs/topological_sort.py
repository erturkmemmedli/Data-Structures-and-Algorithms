def DFS(adjacency_list):
    global clock
    post = [[i, 0] for i in range(len(adjacency_list))]
    visited = [False for _ in range(len(adjacency_list))]
    for vertex in range(len(adjacency_list)):
        explore(adjacency_list, vertex, visited, post)
    return post

def postvisit(post, vertex):
    global clock
    post[vertex][1] = clock
    clock += 1

def explore(adjacency_list, vertex, visited, post):
    global clock
    if visited[vertex] == False:
        visited[vertex] = True
        for neighbor in adjacency_list[vertex]:
            if explore(adjacency_list, neighbor, visited, post):
                return 1
        postvisit(post, vertex)
    return 0

def TopologicalSort(adjacency_list):
    traversal = DFS(adjacency_list)
    traversal = sorted(traversal, key = lambda x: x[1], reverse = True)
    order = [traversal[i][0] + 1 for i in range(len(traversal))]
    return order

if __name__ == '__main__':
    vertex, edge = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(edge)]
    adjacency_list = [[] for _ in range(vertex)]
    for a, b in edges:
        adjacency_list[a - 1].append(b - 1)
    global clock
    clock = 1
    print(*TopologicalSort(adjacency_list))