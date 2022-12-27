# Mock interview with Bahruz Abil (Microsoft)

# Q1 - LeetCode 41

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

# Q2 - Circular Deque with Array

class CircularQueueWithArray:
    def __init__(self, size):
        assert size > 0, "array has no size"
        self.array = [None] * size
        self.size, self.head, self.tail = size, 0, 0
        
    def enqueue(self, val):
        assert self.array[self.tail] == None, "array is full"
        self.array[self.tail] = val
        self.tail = (self.tail + 1) % self.size
        print(self.array)
        
    def dequeue(self):
        assert self.array[self.head] != None, "array is empty"
        result = self.array[self.head]
        self.array[self.head] = None
        self.head = (self.head + 1) % self.size
        print(self.array)
        return result
        
    def front(self):
        assert self.array[self.head] != None, "array is empty"
        print(self.array)
        return self.array[self.head]
