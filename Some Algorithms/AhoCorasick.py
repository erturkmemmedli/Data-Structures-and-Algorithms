from typing import Optional, List, Deque, Dict
from collections import deque


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.output = []
        self.fail = None


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert_into_trie(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.output.append(word)
        
    def build_trie(self, words: List[str]) -> None:
        for word in words:
            self.insert_into_trie(word)
        
    def build_fails(self) -> None:
        queue = deque()
        for node in self.root.children.values():
            queue.append(node)
            node.fail = self.root
        self.bfs_trie(queue)
            
    def bfs_trie(self, queue: Deque[Optional[TrieNode]]) -> None:
        while queue:
            current_node = queue.popleft()
            for key, next_node in current_node.children.items():
                queue.append(next_node)
                fail_node = current_node.fail
                while fail_node and key not in fail_node.children:
                    fail_node = fail_node.fail
                next_node.fail = fail_node.children[key] if fail_node else self.root
                next_node.output.extend(next_node.fail.output)
    
class AhoCorasick:
    def __init__(self, words: List[str]) -> None:
        self.trie = Trie()
        self.words = words
        self.trie.build_trie(words)
        self.trie.build_fails()
    
    def search_text(self, text: str) -> Dict[str, List[int]]:
        root = self.trie.root
        result = {word: [] for word in self.words}
        current_node = root
        for i, char in enumerate(text):
            while current_node and char not in current_node.children:
                current_node = current_node.fail
            if not current_node:
                current_node = root
                continue
            current_node = current_node.children[char]
            for word in current_node.output:
                result[word].append(i - len(word) + 1)
        return result
        

if __name__ == '__main__':
    genes = ['acgtt', 'agct', 'ccgt', 'acttg', 'gccat', 'cagat', 'tagac', 'gtagcatga', 'gtag']
    text = 'accgactgtgcgctgagagcagcatgacttgacgagagtacgtagcatgacagagatccgtgatgatcagattgtagaccgt'
    aho_corasick = AhoCorasick(genes)
    matches = aho_corasick.search_text(text)
    print(matches)
