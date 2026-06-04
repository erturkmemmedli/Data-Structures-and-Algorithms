# Mock interview with Rufat Eyvazli (Meta)

'''
A thief has found a new area to rob. The entrance leads into a neighborhood shaped like a binary tree. 
Each house (node) has a certain amount of money. 
The security system is set up so that if two directly-linked houses are robbed on the same night, the police will be automatically contacted.
Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

int rob(TreeNode* root) {}

TC: O(n)
SC: O(n/2 -> h)

			     30 ->52,22
  
  		 2 ->2,9		   20->20,13
    
   4 ->4,0  5 ->5,0	   6->6,0    7->7,0
   
   
   Input: root = [3,2,3,null,3,null,1]
   
   				3  # left: (2,3),  right:(3, 1)
               / \
              2	  3
               \   \
                3   1
'''
  
def rob(root: TreeNode) -> int:
  def dfs(node: TreeNode) -> list[int]:
    if not node:
      return 0, 0
    
    l = dfs(node.left)
    r = dfs(node.right)
    
    a = node.val + l[1] + r[1]
    b = max(l) + max(r)
    return a, b 
    
  outcome = dfs(root) 
  return max(outcome)

'''
The security company has upgraded.
Now the police are alerted if any two robbed houses are fewer than K edges apart in the neighborhood tree. 
Given the tree and integer K, return the maximum money the thief can steal. (The original problem is K=2.)

TC: O(n * k)
SC: O(h * k)

			1
  		  2
        3
      4
    5
    
    k=3
    
    [5,0,0]
    [4,5,0]
    [3,4,5]
    [7,3,4]
    [5,7,3]
'''
  
def rob(root: TreeNode) -> int:
  def dfs(node: TreeNode) -> list[int]:
    if not node:
      return [0] * k
    
    l = dfs(node.left)
    r = dfs(node.right)
    
    result_set = [0] * k
    
    for i in range(k):
      if i == 0:
      	result_set[i] += l[-i-1] + r[-i-1] + node.val
      else:
        result_set[i] = max(l) + max(r)

    return result_set
    
  outcome = dfs(root) 
  return max(outcome) 

'''
def rob(root: TreeNode, k: int) -> int:
    def dfs(node: TreeNode) -> list[int]:
        if not node:
            return [0] * k
        
        l = dfs(node.left)
        r = dfs(node.right)
        
        state = [0] * k

        state[0] = node.val + l[1] + r[1]
        
        for d in range(1, k):
            if d + 1 >= k:
                state[d] = max(l) + max(r)
            else:
                state[d] = l[d + 1] + r[d + 1]
        
        return state
    
    return max(dfs(root))  
'''
