# Mock Interview with Tural Farhadov (MongoDB)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.all_subsets = []
        self.backtrack(nums, [])
        return self.all_subsets

    def backtrack(self, nums, path):
        # lock
        self.all_subsets.append(path)
        # unlock

        if not nums:
            return
            
        for i in range(len(nums)):
            path.append(nums[i])
            self.backtrack(nums[i+1:], path)
            path.pop()

# Follow up: Mulitple threads
