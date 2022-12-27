# LeetCode 41

# Difference from leetcode is negative numbers are not included.

# Couldn't find O(n) solution but suggested amortized O(n) with heap solution.
# Interviewer asked to design heap but then allowed to use built-in heap function.
# However, implementation of minHeap, maxHeap must be studied again.

from heapq import heapify, heappop

class Solution:
    def firstMissingPositive(self, nums):
        heapify(nums)
        start = 1
        while nums:
            pop = heappop(nums)
            if pop == 0:
                continue
            elif pop > start:
                return start
            else: 
                start += 1
        return start if pop == 0 else pop + 1
