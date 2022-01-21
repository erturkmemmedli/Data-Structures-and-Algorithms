import sys
import threading
import time
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

class tree_height():
    
    def __init__(self):
        self.n = 0
        self.parents = []
        self.generation = []

    def read_input(self):
        self.n = int(input())
        self.parents = list(map(int, input().split()))
        self.generation = [0] * self.n
        
    def recursion(self, child):
        if self.parents[child] == -1:
            return 1
        if self.generation[child] != 0:
            return self.generation[child]
        else:
            self.generation[child] = 1 + self.recursion(self.parents[child])
            return self.generation[child]
        
    def compute_height(self):
        
        return max([self.recursion(i) for i in range(self.n)])

def main():
    tree = tree_height()
    tree.read_input()
    print(tree.compute_height())
    
threading.Thread(target=main).start()
time.sleep(1)