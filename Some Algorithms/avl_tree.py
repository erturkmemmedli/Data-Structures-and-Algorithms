class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    def __init__(self):
        self.root = None
        self.size = 0
        		
    def height(self, node):
        return node.height if node else 0
		
    def setHeight(self, node):
        return 1 + max(self.height(node.left), self.height(node.right)) if node else 0
    
    def rightRotate(self, node):
        new_root = node.left
        node.left = node.left.right
        new_root.right = node
        node.height = self.setHeight(node)
        new_root.height = self.setHeight(new_root)
        return new_root
    
    def leftRotate(self, node):
        new_root = node.right
        node.right = node.right.left
        new_root.left = node
        node.height = self.setHeight(node)
        new_root.height = self.setHeight(new_root)
        return new_root
        
    def insert(self, node, val):
        if node == self.root:
            self.size += 1
        if node is None:
            return Node(val)
        if node.val < val:
            node.right = self.insert(node.right, val)
        else:
            node.left = self.insert(node.left, val)
        balance = self.height(node.left) - self.height(node.right)
        if balance > 1:
            if self.height(node.left.left) > self.height(node.left.right):
                node = self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                node = self.rightRotate(node)
        elif balance < -1:
            if self.height(node.right.right) > self.height(node.right.left):
                node = self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                node = self.leftRotate(node)
        else:
            node.height = self.setHeight(node)
        return node 
    
    def getMinValNode(self, node):
        return self.getMinValNode(node.left) if node and node.left else node        
    
    def remove(self, node, val):
        if node is None:
            return
        if node.val < val:
            node.right = self.remove(node.right, val)
        elif node.val > val:
            node.left = self.remove(node.left, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                right_min_val_node = self.getMinValNode(node.right)
                node.val = right_min_val_node.val
                node.right = self.remove(node.right, right_min_val_node.val)
        node.height = self.setHeight(node)
        balance = self.height(node.left) - self.height(node.right)
        if balance > 1:
            if self.height(node.left.left) > self.height(node.left.right):
                node = self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                node = self.rightRotate(node)
        elif balance < -1:
            if self.height(node.right.right) > self.height(node.right.left):
                node = self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                node = self.leftRotate(node)
        else:
            node.height = self.setHeight(node)
        return node
    
    def predecessor(self, node, val):
        if node is None:
            return
        if node.val == val:
            return val
        elif node.val > val:
            return self.predecessor(node.left, val)
        else:
            right_res = self.predecessor(node.right, val)
            return right_res if right_res else node.val    
						
    def successor(self, node, val):
        if node is None:
            return
        if node.val == val:
            return val
        elif node.val < val:
            return self.successor(node.right, val)
        else:
            left_res = self.successor(node.left, val)
            return left_res if left_res else node.val
    
# tree = AVLTree()
# root = tree.root
