# Mock Interview with Tural Farhadov (MongoDB)

list[nums]

[1,2,3,4] > sorted order.
[1,4,9,16] > sorted order.

[-5,-3,1,4,5,6]	
[1,-3,4,-5,5,6]

[36, 25, 25, next]
[None] * len(nums)

O(k*N) = O(N)

def find_squares(nums):
		min_idx = 0
    min_val = float('inf')
    
    for i, num in enumerate(nums):
    		if abs(num) < min_val:
        		min_val = abs(num)
            min_idx = i
            
    output = [min_val ** 2]
    
    i, j = min_idx - 1, min_idx + 1
  	
    # -1, 0, 4, 5, 6
    
    while i >= 0 or j < len(nums):
    		leftVal, rightVal = -inf, -inf
    		if i >= 0 :
        	  // update the left value
        		output.append(nums[j] ** 2)
            j += 1
            continue
        if j <len(nums):
        		// update the rightvalue
        		output.append(nums[i] ** 2)
            i -= 1
            continue
        
    		output.append(max(left, right))
    
    return output
    
    
	Ø Good 
		○ Clarifying questions
			§ integers?
			§ Negtive numbers?
			
	Ø Bad
		○ Clarifying sorted 
		○ Equals
		○ Test your code, don't be confident on the code you just wrote
		○ Ask can I change the input. Should the solution be-place
		

    
                      
            
