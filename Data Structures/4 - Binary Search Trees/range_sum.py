class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
    if v == None:
        return
    v.sum = v.key + ((v.left.sum if v.left != None else 0)) + ((v.right.sum if v.right != None else 0))
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v

def smallRotation(v):
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v

def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        smallRotation(v.parent)
        smallRotation(v)
    else:
        smallRotation(v)
        smallRotation(v)

def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v

def find(root, key):
    v = root
    last = root
    next = None
    while v != None:
        if v.key >= key and (next == None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return (next, root)

def split(root, key):
    (result, root) = find(root, key)
    if result == None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)

def merge(left, right):
    if left == None:
        return right
    if right == None:
        return left
    while right.left != None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right

root = None

def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right == None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)

def leftDescendant(n):
    if (n.left == null):
        return n
    else:
        return leftDescendant(n.left)

def rightAncestor(n):
    if n.key < n.parent.key:
        return n.parent
    else:
        return rightAncestor(n.parent)

def Next(node):
    if node.right != None:
        return leftDescendant(node.right)
    else:
        return rightAncestor(node)

def deleteNode(node):
    global root
    if node.right == None:
        root = node.left
    else:
        temp = Next(node)
        node = temp
        root = node.right
        root.left = node.left
    if (root != None):
        root.parent = None
    update(root)

def erase(key):
    global root
    points = find(root, key + 1)
    next_node = points[0]
    if next_node != None:
        splay(next_node)
    node = points[1]
    if node != None:
        if node.key == key:
            deleteNode(node)

def search(key):
    global root
    if (root == None):
        return False
    if (root.key == key):
        return True
    elif (root.key > key):
        if (root.left == None):
            return False
        else:
            root = root.left
            return search(key)
    elif (root.key < key):
        if (root.right == None):
            return False
        else:
            root = root.right
            return search(key)
    return False

def sum(from_point, to_point):
    global root
    (left, middle) = split(root, from_point)
    (middle, right) = split(middle, to_point + 1)
    answer = 0
    if (left != None and left.key >= from_point and left.key <= to_point):
        answer += left.sum
    if (middle != None and middle.key >= from_point and middle.key <= to_point):
        answer += middle.sum
    if (right != None and right.key >= from_point and right.key <= to_point):
        answer += right.sum
    root = merge(merge(left, middle), right)
    return answer

if __name__ == '__main__':
    M = 1000000001
    n = int(input())
    x = 0
    data = input().split()
    i = 0
    operation = []
    while i < len(data):
        if data[i] in ['-', '+', '?']:
            operation.append(data[i:i+2])
            i += 2
            continue
        if data[i] == 's':
            operation.append(data[i:i+3])
            i += 3
            continue
    for j in range(n):
        if operation[j][0] == '+':
            insert((int(operation[j][1]) + x) % M)
        elif operation[j][0] == '-':
            erase((int(operation[j][1]) + x) % M)
        elif operation[j][0] == '?':
            print ('Found' if search((int(operation[j][1]) + x) % M) else 'Not found')
        elif operation[j][0] == 's':
            result = sum((int(operation[j][1]) + x) % M, (int(operation[j][2]) + x) % M)
            print(result)
            x = result % M
