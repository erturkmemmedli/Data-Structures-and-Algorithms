# Mock interview with Adil Adilli (Google)

'''
Part 1
Let's define a kind of message called "Broadcast & Shut Down." When a router receives this message, it broadcasts the same message to all other routers within its wireless range. Then, that  shuts down, and can no longer send or receive messages.

For example, Router A is at (0, 0); Router B is at (0, 8); Router C is at (0, 17); Router D is at (11, 0). If the wireless range is 10, when Router A sends a message, it could first reach B; the message from Router B would further reach Router C but Router D would never receive this message.

Given a list of routers' locations (their names and the corresponding 2D coordinates), tell me whether a message from Router A can reach Router B. Write a method / function with appropriate input and output arguments.

Part 2
Initially, all the routers start as powered-on. Assume that a broadcast only transmits to the nearest powered-on router(s). If there are multiple powered-on router(s) that are at the same distance away from the transmitting router, all of them will receive the message and continue the broadcast chain.
'''

A-> B
B->C
|
v
D

# Graph construction
# T: o(n^2) S: o(n^2)
# traversal
# T: O(n+e) O(n)

class Solution:
    def broadcastAndShutDown(self, locations, source, destionation, wirelessRange) -> bool:
        # graph construction
        n = len(locations)
        graph = [[] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                self.insideCircle(graph, i, j, n[i], n[j], wirelessRange)
            
        # breadth-first search
        queue = collections.deque([0, source])
        visited = {source}
        while queue:
            distance, node = queue.popleft()
            if node == destionation:
                return True
            smallest = []
            # part 2 code here => checking smallest distances and adding them to smallest list
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
        return False

    def insideCircle(self, graph, node1, node2, coord1, coord2, wirelessRange):
        x1, y1 = coord1
        x2, y2 = coord2
        distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if distance <= wirelessRange ** 2:
            graph[node1].append((distance, node2))
            graph[node2].append((distance, node1))

# (distance, node)
# o(n^2*log(n))

print('expected:',False, 'actual:', object.broadcastAndShutDown())
assert a==b, f'{a} is not equal to {b}'
