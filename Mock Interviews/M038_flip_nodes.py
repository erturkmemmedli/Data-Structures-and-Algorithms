# Mock interview with Adil Adilli (Salesforce)

'''
You have a binary tree with n nodes labeled from 1 to n. The tree structure follows a specific pattern:

Node 1 is the root
For any node with label v, its parent is the node with label floor(v / 2)
This means node 2 and node 3 are children of node 1, nodes 4 and 5 are children of node 2, and so on
Initially, all nodes have a value of 0.

You're given an array queries where each queries[i] represents a node label. 
For each query, you need to flip the values in the entire subtree rooted at that node (including the node itself). 
Flipping means changing 0 to 1 and 1 to 0.

After processing all queries in order, you need to return the total count of nodes that have value 1.

Example of tree structure when n = 7:

Node 1 is the root
Node 3 has parent floor(3/2) = 1
Node 7 has parent floor(7/2) = 3
The tree forms a complete binary tree pattern where:

Node i has left child 2*i and right child 2*i + 1 (if they exist within range 1 to n)

'''

tree = [0, 0, 0, 0, 0] -> n
 		1  2  3  4  5
  
queries = list[int] -> [1, n] -> m

2*i, 2*i+1

TC: O(m * n)
SC: O(n)
  
def flip_nodes(n: int, queries: list[int]) -> int: # n = 5, queries = [4, 2]
  tree = [0] * n # [0, 0, 0, 0, 0]
  
  for node in queries:
    queue = deque([node]) # [4, 5]
    
    while queue:
      size = len(queue) # 2
      
      for _ in range(len(size)):
        curr_node = queue.popleft() # 5
        tree[curr_node - 1] ^= 1 # [0, 1, 0, 0, 1]
        
        left = curr_node * 2 # 10
        right = curr_node * 2 + 1 # 11
        
      	if left <= n:
          queue.append(left)
          
        if right <= n:
          queue.append(right)
  
  return sum(tree) # 2
  
  	
  [4, 2]
  [0, 0, 0, 1, 0]
  
  
  
def flip_nodes(n: int, queries: list[int]) -> int: # n = 5, queries = [4, 2]
  tree = [0] * n # [0, 0, 0, 0, 0]
  
  # optimization with counter
  counter = Counter(queries)
  modified_queries = [k for k, v in counter.item() if v & 1 == 1]
  
  for node in modified_queries:
    queue = deque([node]) # [4, 5]
    
    while queue:
      size = len(queue) # 2
      
      for _ in range(len(size)):
        curr_node = queue.popleft() # 5
        tree[curr_node - 1] ^= 1 # [0, 1, 0, 0, 1]
        
        left = curr_node * 2 # 10
        right = curr_node * 2 + 1 # 11
        
      	if left <= n:
          queue.append(left)
          
        if right <= n:
          queue.append(right)
  
  return sum(tree) # 2


# Optimization: eliminating next children.
