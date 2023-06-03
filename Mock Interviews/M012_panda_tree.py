# Mock Interview with Adil Adilli (Google)

# 1
# Given an unrooted tree with all of the nodes having at most 3 neighbors. Please find a node in a tree so that after setting the node as root it forms a valid binary tree.
# it is a valid tree, nodes are connected

'''
[[1,2,3],[0],[0],[0]]
 
     1 - 0 - 2 - 4
        |
        3
'''

'''
2
Given an unrooted tree with all of the nodes having at most 3 neighbors. Every node is colored either in black or white. Please find a root node so that:

1. It will form a valid binary tree.
2. Nodes with the same depth are colored with the same color.
3. Color should alternate between black and white between layers. (root can be any color, so it can be B->W->B->… or W->B->W->… starting from root).
Return -1 if we can’t find such a node.
tree = [[[1,2],[0, 3],[0],[1]]]
colors = ['w','b',''w,'w']

3 - 1 - 0 - 2
w   b   w   w  
1 - b 
0, 3 - w
'''

'''
3
Given an unrooted tree with all of the nodes having at most 3 neighbors. Every node is colored either in red or black or white. Please find a root node so that:

1. It will form a valid binary tree.
2. Nodes with the same depth are colored with the same color.
3. Color should be changing in R->W->B->R->W->B order as depth increases. Please note that R->B->W->R->B->W is not allowed. (root can be any color, so it can be R->W->B->… or W->B->R->… or B->R->W->… starting from root)
Return -1 if we can’t find such a node.
'''

class TreeRoot:
    def find_root(self, tree):
        for node in tree:
            if len(node) < 3:
                return node

    def is_alternating(self, tree, colors):
        starting_node = 0

        while starting_node < len(tree):
            if len(tree[starting_node]) < 3:
                break
            
            starting_node +=1

        queue = deque([starting_node])
        visited = {starting_node}

        while queue:
            node = queue.popleft()
            current_color = colors[node]

            for neighbor in tree[node]:
                if colors[neighbor] == current_color:
                    return -1

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return starting_node

'''        
[[[1,2],[0, 3],[0],[1]]]
colors = ['w','b','b','w']
node = 0, w

queue = [ 3]

node = 1, b
node = 2, b

'''

'''
1. find node with less than 3 neighbors
2. traverse from that node bfs to check alternating condition
    2a. if success return node value
    2b. if fail return -1
'''










