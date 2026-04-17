# Mock interview with Adil Adilli (Salesforce)

'''
There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
a is a prefix of b and a.length < b.length.
'''

# ["ab", "abc"]
# ["abc", "ab"]

# O(N*M) -> n: len of input, M: len of biggest char.
# O(N + M)
# O(K * K)

# ["ab", "ac", "ab", "ac"] => ""
# ["ab", "ac"] => ""

from collections import defaultdict

# ex3:  ["a", "ba", "bb"]

def find_order(words: list[str]) -> str:
  graph = defaultdict(set)
  indegree = defaultdict(int)
  
  for word in words:
    for char in word:
      graph[char] = set()
      indegree[char] = 0
      
  # graph = {a: [], b: [c, c], c: [b]}
  # indegree = {a: 0, b: 1, c: 2}
  
  # ["ab", "ac"] => "abc"
  
  # graph = {a: [], b: [c], c: []}
  # indegree = {a: 0, b: 0, c: 1}
  
  # ex3:
  # graph: a: [], b: []
  # indegree: a: 0, b: 0
  
  for i in range(1, len(words)):
    curr = words[i]
    prev = words[i - 1]
    
    m, n = len(prev), len(curr)
    
    # prev = ab, curr = ac
    
    for i in range(min(m, n)):
      if curr[i] != prev[i]:
        graph[prev[i]].add(curr[i]) 
        indegree[curr[i]] += 1
        break
    else:
      if i < m - 1:
        return ""

  # graph = {a: [], b: [c, c], c: [b]}
  # indegree = {a: 0, b: 1, c: 2}
  
  # ex 2
  # graph = {a: [], b: [c], c: []}
  # indegree = {a: 0, b: 0, c: 1}
  
  # ex 3:
  # graph: a: [b, b], b: []
  # indegree: a: 0, b: 2
  
  queue = deque([node for node in indegree if indegree[node] == 0])
  toposort = []
  
  # queue: [a]
  # toposort = []
  
  # ex2
  # queue = [a, b]
  
  # ex3
  # queue = [a]

  while queue:
    node = queue.popleft() # a
    toposort.append(node) # [a, b]
    
    for neighbor in graph[node]: # c
      indegree[neighbor] -= 1
      # indegree = {a: 0, b: 0}
      if indegree[neighbor] == 0:
        queue.append(neighbor)
         # queue = [b]
    
  if len(toposort) == len(graph): # ok
    return "".join(toposort) # abc
  else:
    return "" # done
      
      
# enthusiasm & passion -> mainly about projects -> mostly on fastaswise, then a bit on cn, azcn, socar.
