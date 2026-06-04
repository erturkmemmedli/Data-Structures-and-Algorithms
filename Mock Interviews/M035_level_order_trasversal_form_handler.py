# Mock interview with Nijat Aydamirov (Salesforce)

1) Given the root of a binary tree, return the level-order traversal of its nodes’ values.

That is, return the values level by level from left to right.

Input:
        3
       / \
      9  20
         / \
        15  7

Output:
[
  [3],
  [9, 20],
  [15, 7]
]

TreeNode:
  val: int
  left: TreeNode
  right: TreeNode
    
input: TreeNode
output: List[List[TreeNode]]
  
n = number of nodes

time: O(n)
space: O(n)

from collections import deque
  
def find_level_order_traversal(root: TreeNode) -> List[List[TreeNode]]:
  queue = deque([[root]])
  output = []
  
  while queue:
    level = queue.popleft()
    output.append(level)
    new_level = []
    
    for node in level:
      if node.left:
        new_level.append(node.left)
      if node.right:
        new_level.append(node.right)

    if new_level:
      queue.append(new_level)
      
  return output

 
2) Return the visible nodes when viewing the tree from the right side.

    1
   / \
  2   3               <--    here
   \   \
    5   4
  /
6
    
output = [1, 3, 4, 6]

def tree_view_from_right(root: TreeNode) -> List[int]:
  queue = deque([[root]])
  output = []
  
  while queue:
    level = queue.popleft()
    output.append(level[-1].val)
    new_level = []
    
    for node in level:
      if node.left:
        new_level.append(node.left)
      if node.right:
        new_level.append(node.right)

    if new_level:
      queue.append(new_level)
      
  return output
  
 
3) Form-handler-service - handles form submission from users - Lambda function 
- Cors Headers
- Response Systemcodes (e.g. 101, 400, 500, 600, etc.)
## - Vault secrets - 
       
form-handler -> user-input (form submission) -> Error message / Thanks for submitting -> www.google.com

        Lambda Start
             ↓
        Fetch config from Redis - too many requests?
             ↓
        Cache locally (TTL every 60 sec) // 
             ↓
        Serve requests

what if less change (once a month) -> read-heavy -> CDN
AWS AppConfig -> dynamic vault
