def traveling_salesman(graph):
    n = len(graph)
    memo = {}

    def backtracking(mask, city):
        if mask == (1 << n )- 1: # finished traversing all the nodes
            return graph[city][0]

        if (mask, city) in memo: # already in memo
            return memo[(mask, city)]
        
        min_cost = float("inf")

        for next_city in range(n):
            if mask & (1 << next_city) == 0: # not visited
                new_mask = mask | (1 << next_city)
                cost = graph[city][next_city] + backtracking(new_mask, next_city)
                min_cost = min(min_cost, cost)
            
        memo[(mask, city)] = min_cost
        return min_cost
    
    return backtracking(1, 0)


if __name__ == '__main__':
    graph = [
        [0, 10, 15, 20],
        [5, 0, 9, 10],
        [6, 13, 0, 12],
        [8, 8, 9, 0]
    ]

    min_cost = traveling_salesman(graph)
    print("Minimum Cost: ", min_cost)
