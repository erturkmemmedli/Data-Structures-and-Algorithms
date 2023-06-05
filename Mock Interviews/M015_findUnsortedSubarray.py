# Mock Interview with Bahruz Abil (Microsoft)

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        left_index = len(nums)
        right_index = -1
        greatest = -float('inf')

        for i in range(len(nums)):
            if greatest <= nums[i]:
                stack.append((nums[i], i))
                greatest = nums[i]
                continue

            while stack and stack[-1][0] > nums[i]:
                val, idx = stack.pop()

            if left_index > idx:
                left_index = idx
            
            right_index = i

        return right_index - left_index + 1 if left_index != len(nums) else 0

        # space: O(n)
        # time: O(n)

        # [1,3,2,2,2]
        # [1,3,2,3,3]
        # [2,3,3,2,4]
        # [5,4,3,2,1]
        # [1,3,5,4,2]
