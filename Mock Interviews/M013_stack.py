# Mock Interview with Asif Mammadov (Splunk)

"""
stack - array

push
pop
size
top
getMin

data type - int
"""

class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.max_size = capacity
        #self.minimum = float('inf')
        
    def push(self, val):
        if len(stack) == self.max_size:
            raise Exception("The stack is full!")

        self.stack.append(val)
        #self.minimum = min(self.minimum, val)

    def pop(self):
        if not stack:
            raise Exception("The stack is empty!")

        self.stack.pop()

    def top(self):
        if not stack:
            raise Exception("The stack is empty!")

        return stack[-1]

    def get_min(self):
        return sorted(self.stack)[0]


# Optimization to get_min was made by using second stack by adding smaller element each time and skipping greater elements.
