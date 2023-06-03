# LC894 - Mock Interview with Tural Farhadov (MongoDB)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        self.memo = {}
        return self.dfs(n)

    def dfs(self, n):
        if n == 1:
            return [TreeNode()]

        if n in self.memo:
            return self.memo[n]

        result = []

        for i in range(1, n, 2):
            left = self.dfs(n - i - 1)
            right = self.dfs(i)
            
            for l in left:
                for r in right:
                    root = TreeNode()
                    root.left = l
                    root.right = r
                    result.append(root)

        self.memo[n] = result
        return self.memo[n]
