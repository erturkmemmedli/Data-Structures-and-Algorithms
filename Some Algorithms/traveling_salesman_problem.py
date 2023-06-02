def TSP(mask, pos, graph, dp, n, visited):
    if mask == visited:
        return graph[pos][0]
    
    if dp[mask][pos] != -1:
        return dp[mask][pos]
    
    minimum = float("inf") 
    
    for city in range(0, n):
        if mask & (1 << city) == 0:
            new = graph[pos][city] + TSP(mask | (1 << city), city, graph, dp, n, visited)
            minimum = min(minimum, new)

    dp[mask][pos] = minimum
    
    for x in dp:
        print(x)
    print()
    
    return dp[mask][pos]


if __name__ == '__main__':

    graph = [[0, 7, 21, 5], 
             [10, 0, 11, 16], 
             [12, 9, 0, 10], 
             [8, 16, 13, 0]]
    
    n = 4
    total = 1 << n
    visited = total - 1
    
    dp=[[-1 for j in range(n)]for i in range(total)]

    for i in range(0, visited):
        for j in range(0, n):
            dp[i][j] = -1

    print(TSP(1, 0, graph, dp, n, visited))
    
