# Mock interview with Tural Farhadov (MongoDB)

'''
webserver -> limited resource 

assume single API endpoint -> api/resource

for x seconds > user can access the resouce y times.

rate limiter
	rolling window of x seconds 
  		every x second a user can access a resouce only y times

n requests -> time: O(y), space: O(n)
'''


from collections import defaultdict, deque
from threding import Lock
  
class RateLimiter:
  def __init__(self, second_window: int, request_count: int):
    self.second_window = second_window
    self.request_count = request_count
    self.storage = defaultdict(deque) # thread-safe data structure
    self._locks = defaultdict(Lock)

  def is_accessible(self, user_id: str, time: int) -> bool:
    with self._locks[user_id].lock():
        while user_id in self.storage and len(self.storage[user_id]) > 0 and time - self.storage[user_id][0] > self.second_window:
            self.storage[user_id].popleft()
        if len(self.storage[user_id]) < self.request_count:
          self.storage[user_id].append(time)
          return True
        return False


rl = RateLimiter(5, 3)
print(rl.is_accessible('A', 2))
print(rl.storage)
print(rl.is_accessible('B', 3))
print(rl.storage)
print(rl.is_accessible('A', 5))
print(rl.storage)
print(rl.is_accessible('A', 6))
print(rl.storage)
print(rl.is_accessible('A', 7))
print(rl.storage)
print(rl.is_accessible('A', 9))
print(rl.storage)
print(rl.is_accessible('B', 10))
print(rl.storage)


# OutOfMemory - Cronjob - TTL (Redis)
# Multithreading - Locking each user based on their user_id saved in locks dict.
# Distributed Cache - Sticky Session (communicated with LoadBalancer to use always Same Webserver)
