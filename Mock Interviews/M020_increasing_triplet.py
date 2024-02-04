# Mock Interview with Tural Ismayilzade (Oracle)

# First Solution

from bisect import bisect_left

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = []

        for num in nums:
            idx = bisect_left(stack, num)

            if idx == len(stack):
                stack.append(num)
            else:
                stack[idx] = num

            if len(stack) == 3:
                return True

        return False

# Second Solution

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = None
        j = None

        for num in nums:
            if i == None or num <= i:
                i = num
            else:
                if j == None or num <= j:
                    j = num
                else:
                    return True

        return False

# O(n) time, O(1) space
