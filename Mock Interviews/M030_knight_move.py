# Mock interview with Adil Adilli (Salesforce)

'''
You are given an 8x8 chessboard, your goal is to find the minimum number 
of knight moves required to reach from source square to destination square.

x = (0, 0), y = (5,4)

O(64)

4,4 -> 5,6 -> ... -> 7,8 (10) ->
4,4 -> ... -> 7,8 (7) 

time complexity = O(n^2 *log(n)) for Dijkstra, O(n^2) for BFS
space complexity = O(n^2)
'''

# [i i i i i i i i]
# [i i i i i i i i]
# [i i i 1 i 1 i i]
# [i i 1 i i i 1 i]
# [i i i i 0 i i i]
# [i i 1 i i i 1 i]
# [i i i 1 i 1 i *]
# [i i i i i 2 i i]

def find_min_knight_move(source, destination): # (4, 4) -> (6, 7)
  distance = [[float('inf')] * 8 for _ in range(8)]
  x, y = source
  t, z = destination
  
  heap = [(0, x, y)] # queue = deque([(0, x, y])
  distance[x][y] = 0 # visieted = set()
  
  while heap:
    d, x, y = heappop(heap) # queue.popleft() - # 0, 4, 4
    
    if x == t, y == z:
      return d
    
    for row, col in (x-1,y-2), (x-1,y+2), (x+1,y-2), (x+1,y+2), (x-2,y-1), \
	    (x-2,y+1), (x+2,y-1), (x+2, y+1): # to be improved later
      if 0 <= row < 8 > col >= 0 and distance[row][col] > d + 1: # (row, col) not in visited
        distance[row][col] = d + 1 # visited.add((row, col)
        heappush(heap, (d+1, row, col)) # queue.append((d+1, row, col))
        
# Follow up 1 - reconstruciton of path

from math import inf
from heapq import heappush, heappop
        
def find_min_knight_move(source, destination): # (4, 4) -> (6, 7)
  distance = [[(inf, None)] * 8 for _ in range(8)]
  x, y = source
  t, z = destination
  
  heap = [(0, x, y)]
  distance[x][y][0] = 0
  
  while heap:
    d, x, y = heappop(heap) # 0, 4, 4
    
    if x == t, y == z:
      path = reconstruct_path(distance, t, z)  
      return d, path
    
    for row, col in (x-1,y-2), (x-1,y+2), (x+1,y-2), (x+1,y+2), (x-2,y-1), \
	    (x-2,y+1), (x+2,y-1), (x+2, y+1): # to be improved later
      if 0 <= row < 8 > col >= 0 and distance[row][col] > d + 1:
        distance[row][col][0] = d + 1
        distance[row][col][1] = (x, y)
        heappush(heap, (d+1, row, col))     

def reconstruct_path(distance, row, col):
  path = [(row, col)]
  
  while distance[row][col][1] is not None:
    row, col = distance[row][col][1]
    path.append((row, col))
    
  return path[::-1]
 
# Follow up 3: infinite board
'''
1. Bidirectional 
2. A* star alogrithm
3. Mathematical calculation
'''

# Feedbacks:
1. requirement & followup -> output forgotten to ask
2. MUST: complexity -> check 2^n style problems
3. dry run before test (syntax check)
4. directly moved to dfs, then wth dijkstra - no need, bfs cool
5. replacement of heap wth queue and distance wth hashset
6. quadant movement (followup 3)
7. dont forget to import dependencies
8. MUST: write your explanation, verbal can be uncomprensible
9. MUST: check multithreaded approach & MapReduce (infinite board)
