import sys, threading, time
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
                
def inorder(tree, inorder_list):
    if tree == None:
        return
    if tree.left != None:
        inorder(tree.left, inorder_list)
    inorder_list.append(tree.key)
    if tree.right != None:
        inorder(tree.right, inorder_list)
            
if __name__ == '__main__':
    n = int(input())
    if n == 0:
        print('CORRECT')
    else:
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
                if node_list[j].key == node_list[input_list[j][1]].key:
                    flag = False
            if input_list[j][2] != -1:    
                node_list[j].right = node_list[input_list[j][2]]
        tree = node_list[0]
        inorder_list = []
        inorder(tree, inorder_list)
        for x in range(n - 1):
            if  inorder_list[x + 1] < inorder_list[x]:
                flag = False
                break
        if flag:
            print('CORRECT')
        else:
            print('INCORRECT')

threading.Thread(target = main).start()
time.sleep(10)