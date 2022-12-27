# LeetCode 207 & 210 with Adil Adilli (Google)

# cycle detection

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            self.graph[b].append(a)
        self.cycleFound = 0
        self.visited = [0] * numCourses
        for i in range(numCourses):
            if self.cycleFound == 1:
                return False
            if self.visited[i] == 0:
                self.cycleDetection(i)
        return True

    def cycleDetection(self, node):
        if self.cycleFound == 1:
            return
        if self.visited[node] == 1:
            self.cycleFound = 1
        if self.visited[node] == 0:
            self.visited[node] = 1
            for neighbor in self.graph[node]:
                self.cycleDetection(neighbor)
            self.visited[node] = 2
            
# follow-up: topological sort

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct the graph inversely
        self.graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            self.graph[a].append(b)
        # topological sort
        self.cycleFound = 0
        self.visited = [0] * numCourses
        self.postorder = []
        for i in range(numCourses):
            if self.cycleFound == 1:
                return []
            if self.visited[i] == 0:
                self.topologicalSort(i)
        return self.postorder

    def topologicalSort(self, node):
        if self.cycleFound == 1:
            return
        if self.visited[node] == 1:
            self.cycleFound = 1
        if self.visited[node] == 0:
            self.visited[node] = 1
            for neighbor in self.graph[node]:
                self.topologicalSort(neighbor)
            self.visited[node] = 2
            self.postorder.append(node)
