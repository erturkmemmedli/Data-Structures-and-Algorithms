# Mock interview tih Adil Adilli (Salesforce)

'''
Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a sequence of bits 
so that it can be stored or sent across a network to be reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. 
There is no additional restriction on how your serialization/deserialization algorithm should work.

Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. You do not necessarily need to follow this format.
'''


'''
input: TreeNode (root)

api: serialize, deserialize

1, 2, 3, null, null, 4, 5
		  1 => 1
     2        3 => 2,3
  	n n      4 5 => 2#,4,5
  n n n n  n n n n  =>4#, 2# ,2# => 8#
  
  1,2,3,2#,4,5,8#

-> 1,2,3,#,#,4,5,#,#,#,#,6,#,#,#

2^0 + 2^1 + ... + 2^n

time: O(num of nodes)
space: O(2 ^ (hight of tree)) -> O(num of nodes)

-># 1,2,3,#2,4,5,#4,6,#3

1 
2, 3
#2, 4, 5
#4, 6, #3 

power = 0
node_count = 2^power
power += 1
'''

from collections import deque

class Codec:

    def serialize(self, root):
        if not root:
            return ""

        queue = deque([root])
        output = [str(root.val)]
        
        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                output.append(str(node.left.val))
            else:
                output.append("#")
            
            if node.right:
                queue.append(node.right)
                output.append(str(node.right.val))
            else:
                output.append("#")
        
        while output and output[-1] == "#":
            output.pop()
        
        return ",".join(output)

    def deserialize(self, data):
        print(data)
        if not data:
            return
        
        nodes = [TreeNode(int(val)) if val != "#" else None for val in data.split(",")]
        j = 1

        for i in range(len(nodes)):
            if j < len(nodes) and nodes[i]:
                nodes[i].left = nodes[j]
            if j + 1 < len(nodes) and nodes[i]:
                nodes[i].right = nodes[j + 1]
            if nodes[i]:
                j += 2
        
        return nodes[0]
