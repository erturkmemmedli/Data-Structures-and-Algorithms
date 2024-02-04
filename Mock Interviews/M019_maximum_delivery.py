# Mock Intetrview with Adil Adilli (Salesforce)
# Asked in Dropbox
'''
[
3 4 16
56 44 21
9 10 12
]
'''

'''
[
3 4 16
5 4 21
6 8 6
]
'''

# time: O(mn)
# space: O(mn)

memo = {}

def find_max_delivery(grid):
		m, n = len(grid), len(grid[0])
    visited = set()
    
    def dfs(row, col):
        if (row, col) in memo:
          	return memo[(row, col)]
        
        max_path = 1
        
        for r, c in (row-1, col), (row, col-1), (row+1, col), (row, col+1):
        		if m > r >= 0 <= c < n and (row, col) not in visited and grid[r][c] > grid[row][col]:
              	visited.add((r, c))
              	max_path = max(max_path, dfs(r, c) + 1)
                visited.remove((r, c))
                
        memo[(row, col)] = max_path    
        return max_path
    
    for i in range(m):
    		for j in range(n):
          	if (i, j) not in visited:
              	visited.add((i, j))
        				dfs((i, j))
                    
    # reconstraction
    max_val = max(memo.values())
    
    for key, val in memo.items():
      	if val == max_val:
        		x, y = key
            break
            
    path = []
      
    while memo[(x, y)] != 1:
      	path.append((x, y))
        
      	for r, c in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
          	if m > x >= 0 <= y < c and memo[(r, c)] == memo[(x, y)] - 1:
                x, y = r, c
              	break
      
      
# division -> most challenging project, most impactful project
# experience -> how company culture changed
