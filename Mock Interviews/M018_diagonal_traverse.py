# Mock Interview with Bahruz Abil (Microsoft)

'''
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

Input: nums = 
[1,2,3],
[4,5,6],
[7,8,9]
Output: [1,4,2,7,5,3,8,6,9]

Input: nums = 

[1,2,3,4,5],
[6,7],
[8],
[9,10,11],
[12,13,14,15,16]

Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

[1,1,14,15,16]
[12,13,14,15,16]

[1,2,3]
[4]
[5,6,7]

[1,2,3,4,5],
[6,7],
[12,13,14,15,16]
[9,10,11],
[8]

'''

def traverse_diagonal(nums):
    # TODO: Hadnle Edge Cases

    # TODO: Prepare array
    
    # TODO: Logic

    row_map = {i : 0 for i in range(nums)} # {0:3, 1:1, 2:2}
    output = [] # 1, 4, 2, 5, 3, 6, 7
    
    for i in range(len(nums)): # i=2
        for j in range(i, -1, -1): # j=0
            if row_map[j] < len(nums[j]):
                output.append(nums[j][row_map[j]])
                row_map[j] += 1

    i = len(nums) - 1 # i = 2

    while i >= 0:
        if row_map[i] == len(nums[i]):
            i -= 1
            continue
          
        for j in range(i, -1, -1): # j=2
            if row_map[j] < len(nums[j]):
                output.append(nums[j][row_map[j]])
                row_map[j] += 1

    return output

