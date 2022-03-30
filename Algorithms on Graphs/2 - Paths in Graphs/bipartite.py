from collections import deque

def BFS(adjacency_list):
    color = [None for _ in range(len(adjacency_list))]
    for i in range(len(adjacency_list)):
        if color[i] is None:
            color[i] = 'W'
            Q = deque([i])
            while len(Q) != 0:
                vertex = Q.popleft()
                for path in adjacency_list[vertex]:
                    if color[path] is None:
                        if color[vertex] == 'W':
                            Q.append(path)
                            color[path] = 'B'
                        if color[vertex] == 'B':
                            Q.append(path)
                            color[path] = 'W'
                    else:
                        if (color[vertex] == 'W' and color[path] == 'W') or (color[vertex] == 'B' and color[path] == 'B'):
                            return 0
    return 1
	
if __name__ == '__main__':
    vertex, edge = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(edge)]
    adjacency_list = [[] for _ in range(vertex)]
    for a, b in edges:
        adjacency_list[a - 1].append(b - 1)
        adjacency_list[b - 1].append(a - 1)
    print(BFS(adjacency_list))