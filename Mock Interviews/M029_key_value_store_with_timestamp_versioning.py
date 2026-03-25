# Mock interview with Tural Farhadov (MongoDB)

# Key value store with timestamp versioning
# set(key, value) - put the timestamp.now() -> monotonically increasing integer
# get(key, timestamp) - value, val.timstamp <= timestamp

# key, value -> string
# timestamp -> integer

# Dict - key: [(ts, val)]
# dict[str: list[list[int, str]]]

def binary_search(values: list[int, str], target: int) -> int:
  	left, right = 0, len(values) - 1
    position = None
    
    while left <= right:
      	mid = left + (right - left) // 2
        
        if values[mid][0] < target:
          	left = mid + 1
        elif values[mid][0] > target:
          	right = mid - 1
        else:
          	position = mid
            left = mid + 1 
          	
      return right if not position else position

class KeyValueStoreWithTimestamp:
  	def __init__(self):
      	self.storage = {}
        self.mu = Mutex()
        
    def set(self, key: str, value: str) -> None:
      	ts = timestamp.now()
        
      	if key not in self.storage:
          	self.storage[key] = []
        
        self.mu.RWLock()
        self.storage[key].append([ts, value])
        self.mu.RWUnLock()


    def get(self, key: str, timestamp: int) -> str | None:
      	if key not in self.storage:
          	return None
      	
      	self.mu.RLock()
      	values = self.storage[key]
        self.mu.RUnLock()
        
        idx = binary_search(values, timestamp)
        return values[idx][1]


# Followup 1 - Multithreaded -> rlock, rwlock -> Mutex (Synchronization)

# Followup 2 - Memory Limitation -> write to file
# for set: lru is evicted to file, get: cache is used
