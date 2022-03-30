from collections import deque

def BFS(adjacency_list, start, end):
    distance = [float('inf') for _ in range(len(adjacency_list))]
    distance[start] = 0
    Queue = deque([start])
    while len(Queue) != 0:
        vertex = Queue.popleft()
        for path in adjacency_list[vertex]:
            if distance[path] == float('inf'):
                Queue.append(path)
                distance[path] = distance[vertex] + 1
                if path == end:
                    return distance[path]
    return -1

if __name__ == '__main__':
    vertex, edge = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(edge)]
    start, end = map(int, input().split())
    start, end = start - 1, end - 1
    adjacency_list = [[] for _ in range(vertex)]
    for a, b in edges:
        adjacency_list[a - 1].append(b - 1)
        adjacency_list[b - 1].append(a - 1)
    print(BFS(adjacency_list, start, end))
