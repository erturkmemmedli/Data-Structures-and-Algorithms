class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
                
def inorder(tree):
    if tree == None:
        return
    if tree.left != None:
        inorder(tree.left)
    print(tree.key, end = ' ')
    if tree.right != None:
        inorder(tree.right)
        
def preorder(tree):
    if tree == None:
        return
    print(tree.key, end = ' ')
    if tree.left != None:
        preorder(tree.left)
    if tree.right != None:
        preorder(tree.right)

def postorder(tree):
    if tree == None:
        return
    if tree.left != None:
        postorder(tree.left)
    if tree.right != None:
        postorder(tree.right)
    print(tree.key, end = ' ') 

if __name__ == '__main__':
    n = int(input())
    input_list = []
    for _ in range(n):
        indices = list(map(int, input().split()))
        input_list.append(indices)
    node_list = []
    for i in range(n):
        node_list.append(Node(input_list[i][0]))
    for j in range(n):
        if input_list[j][1] != -1:
            node_list[j].left = node_list[input_list[j][1]]
        if input_list[j][2] != -1:    
            node_list[j].right = node_list[input_list[j][2]]
    tree = node_list[0]
    inorder(tree)
    print("\n", end = '')
    preorder(tree)
    print("\n", end = '')
    postorder(tree)