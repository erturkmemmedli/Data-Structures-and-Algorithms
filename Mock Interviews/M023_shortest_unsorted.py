# Mock interview with Bahruz Abil (Microsoft)

'''
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.


1. Clarify
    - I/O 
    - Valid
    - Edge case
    - Limit
    - Duplication
2. Solution
    - s1 brute force
    - s2 
3. Implement
    

4. Manual execution



Solution 1 (Brute Force)
T: TODO
S: TODO

Solution 2 (Backtrack)



Ex:

[2,6,4,8,10,2,9,15]
5

[6,7,5,8,9,1,10,11,8,15,16,17]

[6,7,15,16,11,12,5,4,25,26,27,18,30,31]

[3,2,1]
'''

def make_sorted(nums):
    start_flag = None # TODO check for default value
    end_flag = None 
    start_stack = []
    end_stack = []

    for i, num in enumerate(nums):
        if start_flag != None:
            while start_stack and start_stack[-1][0] > num:
                val, idx = start_stack.pop()
                start_flag = idx
            if start_flag == 0:
                break
        else:
            if not start_stack or start_stack[-1][0] < num:
                start_stack.append((num, i))
            else:
                while start_stack and start_stack[-1][0] > num:
                    val, idx = start_stack.pop()
                    start_flag = idx
            
    for i in range(len(nums) - 1, -1, -1):
        if end_flag != None:
            while end_stack and end_stack[-1][0] < nums[i]:
                val, idx = end_stack.pop()
                end_flag = idx
            if end_flag == len(nums) - 1:
                break
        else:
            if not end_stack or end_stack[-1][0] >nums[i] :
                end_stack.append((nums[i], i))
            else:
                while end_stack and end_stack[-1][0] < nums[i]:
                    val, idx = end_stack.pop()
                    end_flag = idx


    return end_flag - start_flag + 1 if start_flag != None and end_flag != None else 0
