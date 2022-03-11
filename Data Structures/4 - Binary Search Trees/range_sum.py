class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None
        self.height = 1
        
def Find(key, root):
    if root == None:
        return root
    if key < root.key:
        if root.left != None:
            return Find(key, root.left)
        else:
            return root
    elif key > root.key:
        if root.right != None:
            return Find(key, root.right)
        else:
            return root
    return root

def Next(node):
    if node.right != None:
        return LeftDescendants(node.right)
    else:
        return RightAncestors(node)

def LeftDescendants(node):
    if node.left == None:
        return node
    else:
        return LeftDescendants(node.left)

def RightAncestors(node):
    if node.parent == None:
        return None
    if node.key < node.parent.key:
        return node.parent
    else:
        return RightAncestors(node.parent)
    
def Insert(key, root):
    if root == None:
        return Node(key)
    if key < root.key:
        root.left = Insert(key, root.left)
        root.left.parent = root
    if key > root.key:
        root.right = Insert(key, root.right)
        root.right.parent = root
    return root

def Delete(key, root):
    if root == None:
        return root
    if key < root.key:
        root.left = Delete(key, root.left)
        if root.left != None:
            root.left.parent = root
    elif key > root.key:
        root.right = Delete(key, root.right)
        if root.right != None:
            root.right.parent = root
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        next_node = Next(root)
        root.key = next_node.key
        root.right = Delete(next_node.key, root.right)
    return root

def AVLInsert(key, root):
    root = Insert(key, root)
    node = Find(key, root)
    root = Rebalance(node)
    return root

def AVLDelete(key, root):
    node = Find(key, root)
    if node.parent != None:
        P = node.parent
    elif Next(node) != None:
        P = Next(node).parent
    else:
        P = node
    root = Delete(key, root)
    if root != None:
        root = Rebalance(P)
    return root

def Rebalance(node):
    if node == None:
        return node
    P = node.parent
    if node.left != None and node.right != None:
        if node.left.height > node.right.height + 1:
            node = RebalanceRight(node)
        elif node.right.height > node.left.height + 1:
            node = RebalanceLeft(node)
    elif node.left != None:
        if node.left.height > 1:
            node = RebalanceRight(node)
    elif node.right != None:
        if node.right.height > 1:
            node = RebalanceLeft(node)
    node.height = AdjustHeight(node)
    if P != None:
        return Rebalance(P)
    return node
    
def AdjustHeight(node):
    if node.left == None and node.right == None:
        return 1
    if node.left != None and node.right != None:
        return 1 + max(AdjustHeight(node.left), AdjustHeight(node.right))
    elif node.left != None:
        return 1 + AdjustHeight(node.left)
    elif node.right != None:
        return 1 + AdjustHeight(node.right)
    
def RebalanceLeft(node):
    R = node.right
    if R.right != None and R.left != None:
        if R.left.height > R.right.height:
            rotated = RotateRight(R)
    elif R.left != None:
        rotated = RotateRight(R)
    rotated = RotateLeft(node)
    rotated.left.height = AdjustHeight(rotated.left)
    rotated.right.height = AdjustHeight(rotated.right)
    rotated.height = AdjustHeight(rotated)
    return rotated

def RebalanceRight(node):
    L = node.left
    if L.left != None and L.right != None:
        if L.right.height > L.left.height:
            rotated = RotateLeft(L)
    elif L.right != None:
        rotated = RotateLeft(L)
    rotated = RotateRight(node)
    rotated.right.height = AdjustHeight(rotated.right)
    rotated.left.height = AdjustHeight(rotated.left)
    rotated.height = AdjustHeight(rotated)
    return rotated
        
def RotateLeft(node):
    R = node.right
    L = R.left
    R.left = R.parent
    R.left.right = L
    if L != None:
        L.parent = R.left
    R.parent = node.parent
    R.left.parent = R
    if R.parent != None:
        if node == R.parent.left:
            R.parent.left = R
        elif node == R.parent.right:
            R.parent.right = R
    return R
    
def RotateRight(node):
    L = node.left
    R = L.right
    L.right = L.parent
    L.right.left = R
    if R != None:
        R.parent = L.right
    L.parent = node.parent
    L.right.parent = L
    if L.parent != None:
        if node == L.parent.right:
            L.parent.right = L
        elif node == L.parent.left:
            L.parent.left = L
    return L

def RangeSum(a, b, root):
    result = []
    node = Find(a, root)
    if node != None:
        while node != None and node.key <= b:
            if node.key >= a:
                result.append(node.key)
            node = Next(node)
    return sum(result)

if __name__ == '__main__':
    tree = None
    M = 1000000001
    x = 0
    n = int(input())
    for _ in range(n):
        operation = input().split()
        if operation[0] == '+':
            node = Find((int(operation[1]) + x) % M, tree)
            if node is None or (node is not None and node.key != (int(operation[1]) + x) % M):
                tree = AVLInsert((int(operation[1]) + x) % M, tree)
            else:
                continue
        elif operation[0] == '-':
            node = Find((int(operation[1]) + x) % M, tree)
            if node is not None and node.key == (int(operation[1]) + x) % M:
                tree = AVLDelete((int(operation[1]) + x) % M, tree)
            else:
                continue
        elif operation[0] == '?':
            node = Find((int(operation[1]) + x) % M, tree)
            if node is not None and node.key == (int(operation[1]) + x) % M:
                print("Found")
            else:
                print("Not found")
        elif operation[0] == 's':
            summ = RangeSum((int(operation[1]) + x) % M, (int(operation[2]) + x) % M, tree)
            x = summ
            print(summ)