import sys
import threading
import time
from collections import namedtuple
Union = namedtuple('Union', ['destination', 'source'])
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.parents = list(range(len(row_counts)))
        self.max_row_count = max(row_counts)

    def find_parent(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.find_parent(self.parents[i])
        return self.parents[i]

    def merge(self, destination, source):
        destination_parent = self.find_parent(destination)
        source_parent = self.find_parent(source)
        if source_parent == destination_parent:
            return self.max_row_count
        else:
            self.parents[source_parent] = destination_parent
            self.row_counts[destination_parent] += self.row_counts[source_parent]
            self.row_counts[source_parent] = 0
            
            if self.row_counts[destination_parent] > self.max_row_count:
                self.max_row_count = self.row_counts[destination_parent]  
            return self.max_row_count

def main():
    n_tables, n_queries = map(int, input().split())
    row_counts = list(map(int, input().split()))
    assert len(row_counts) == n_tables
    db = Database(row_counts)
    union = []
    data = list(map(int, input().split()))
    for i in range(0, len(data), 2):
        destination, source = data[i], data[i+1]
        union.append(Union(destination - 1, source - 1))
    for table in union:
        print(db.merge(table[0], table[1]))

threading.Thread(target=main).start()
time.sleep(10)