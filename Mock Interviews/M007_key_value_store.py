# Mock interview with Tural Farhadov (MongoDB)

Question: 
Design a DS that would represent a key-value store.

single key and single value
keys are integers, values are arbitary types

R1: 0<=key<=10000
R2: 100<=key<=1000
R3:
insert(1,4)
insert(2,5)
insert(3,5)
getElements() -> string {1->4, 2->5, 3->5}

class KeyValueStore:
    def __init__(self, start, end):
        self.map = [None] * (end - start + 1)
    
    def insert(self, key: int, value: int) -> None:
        # if not _validate(key): return False
        assert 100 <= key <= 1000, "You should give a key in the range of [100, 1000]"
        self.map[key - 100] = value
        #return True

    def remove(self, key):
        assert 100 <= key <= 1000, "You should give a key in the range of [100, 1000]"
        self.map[key - 100] = None

    def show(self, key):
        assert 100 <= key <= 1000, "You should give a key in the range of [100, 1000]"
        return self.map[key - 100]

    def getElements(self):
        elements = ""
        for i in range(100, 1001):
            if self.map[i]:
                if i != 1000:
                    elements += str(i) + "->" + str(self.map[i]) + ', '
                else:
                    elements += str(i) + "->" + str(self.map[i])

    # method names must be verbs
    def _validate(self, key):
        return type(key) = 'int' and 100 <= key <= 1000

1.. good: clarifying questions. 
    good: range, type. 
2.. bad: discussion on implemention. 
    would be good: size calculation - integer (4 byte)
