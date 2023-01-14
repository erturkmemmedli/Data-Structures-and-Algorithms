# Mock interview with Bahruz Abil (Microsoft)

'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

1 clarify
    array
    distinct
    range 


1) clarify questions: 

Input: nums = [3,0,1]
Output: 2

- not sorted
- n element, 1 missing over n+1 elements
- n < 10000
- 0 and n including

2) solution

- sorting array -> time: O(nlogn), space: O(n)/O(1)
- hashset solution -> time: O(n), space: O(n)

n = 7
{0, ..., 6}
int a = 0
if inside: a++
else: return
- time: O(n), space: O(1)

- sum(nums) and subtraction - T: O(n), S: O(1)

[100,4,1,32,20]
change all  nums not in range [0-4] to -1
[-1,1,-1,-1,4]

'''
