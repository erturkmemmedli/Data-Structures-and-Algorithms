# Movk Interview with Tural Ismayilzade (Oracle)

class ListNode:

    def __init__(self, key, value, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        node.next = None

        if not self.head:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next

    def remove(self, node):
        if node == self.head:
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next

            else:
                self.head = None
                self.tail = None

        elif node == self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev

        else:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_cache = {}
        self.linked_list = DoublyLinkedList()

    def get(self, key: int) -> int:
        # print(self.lru_cache)

        if key not in self.lru_cache:
            return -1

        node = self.lru_cache[key]
        self.linked_list.remove(node)
        self.linked_list.insert(node)

        # temp = self.linked_list.head
        # l = []
        # while temp:
        #     l.append(temp.value)
        #     temp = temp.next
        # print(l)

        return self.lru_cache[key].value
        

    def put(self, key: int, value: int) -> None:
        # print(self.lru_cache)

        if key in self.lru_cache:
            node = self.lru_cache[key]
            self.linked_list.remove(node)
            node.value = value
            self.linked_list.insert(node)
            return

        if self.capacity:
            node = ListNode(key, value)
            self.lru_cache[key] = node
            self.linked_list.insert(node)
            self.capacity -= 1

        else:
            head = self.linked_list.head
            self.linked_list.remove(head)
            del self.lru_cache[head.key]
            node = ListNode(key, value)
            self.lru_cache[key] = node
            self.linked_list.insert(node)

        # temp = self.linked_list.head
        # l = []
        # while temp:
        #     l.append(temp.value)
        #     temp = temp.next
        # print(l)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
