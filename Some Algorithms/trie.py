class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = self.get_node()
    
    def get_node(self):
        return TrieNode()
    
    def indexing(self, char):
        return ord(char) - ord('a')
    
    def insert(self, word):
        temp = self.root
        for i in range(len(word)):
            index = self.indexing(word[i])
            if not temp.children[index]:
                temp.children[index] = self.get_node()
            temp = temp.children[index]
        temp.end = True
            
    def search(self, word):
        temp = self.root
        for i in range(len(word)):
            index = self.indexing(word[i])
            if not temp.children[index]:
                return False
            temp = temp.children[index]
        return temp.end
