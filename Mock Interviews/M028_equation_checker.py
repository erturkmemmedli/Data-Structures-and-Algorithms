# Mock interview with Adil Adilli (Salesforce)

'''

"a=b"
"c!=b"

1. add all the equalties
2. check for inequalities
'''

'''
solution: UnionFind
TC: O(nlogn) -> O(n)
SC: O(n)

'''

# [a=b, b=c, g=h, h=c, d!=g] -> false
# [a=b, b=a] -> True
# [a=b, b!=a] -> False
# [a=b, b=a] -> True
class UnionFind:
  	def __init__(self):
      	self.parent = list(range(26))
        self.rank = [0] * 26
        
      def find(self, node):
        	while node != self.parent[node]:
            	node = self.parent[node]
          return node
        
      def union(self, node1, node2):
        	root1 = self.find(node1) # 6
          root2 = self.find(node2)	# 0
          
          if root1 != root2:
            	if self.rank[root1] < self.rank[root2]:
                	self.parent[root1] = root2
              elif self.rank[root2] < self.rank[root1]: # [0, 0, 0, ...]
                	self.parent[root2] = root1  # [1, 0, 0 ...]
              else:
                	self.parent[root2] = root1 # [6, 0, 0, 3, 4, 5, 6, 6...]
                  self.rank[root1] += 1  		 # [1, 0, 0, 0, 0, 0, 2, 0, ...]
            	return True
          
          return False
parent [1,0,0,3,4]
rank   []
def are_valid_equations(equations):
    nonequals = []
    uf = UnionFind()
    
    for equation in equations:
      	if len(equation) == 3:
          	node1 = ord(equation[0]) - ord('a') # 3
            node2 = ord(equation[2]) - ord('a')	# 6
          	uf.union(node1, node2)
        else:
          	nonequals.append(equation)
            
    for equation in nonequals:
        node1 = ord(equation[0]) - 97 # 3
        node2 = ord(equation[3]) - 97 # 6
        
        parent1 = uf.find(node1) #0
        parent2 = uf.find(node2)	#g-idx
        
        if parent1 == parent2:
          	return False
          
    return True

'''
"a=b"
"c!=b"
"d>a"
"b>d"

Topological Sort

set1		set2
a				c
b				d

a->c
d->b
'''  

Erturk Feedback

Good asking questions
- return any paths?

Explain the brute force first and then move into alternative /better solutions


good going through your solution

Turkish accent horrible


————— 
Mar 2, 2024
- good asking about input
	- english letters
	- one letter
	- duplicates

- talk about complexity
- explain by illustrating instead of showing with your hands(ranks question)
- -‘a’
- solution ustunden key sehvin versa duzelt here tea yazmadan
- simple examplelerden istifade ale
- use tabular representation for debugging

            
            
