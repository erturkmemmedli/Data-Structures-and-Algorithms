class MinHeap:
    def __init__(self, array):
        self.heap = array

    def push(self, num):
        self.heap.append(num)
        self.sift_up(num, len(self.heap) - 1)

    def pop(self):
        self.heap[0] = float('inf')
        min_element = self.sift_down()
        self.heap.pop()
        return min_element

    def sift_up(self, num, current_idx):
        while current_idx:
            if current_idx % 2 == 0:
                parent_idx = (current_idx - 2) // 2
            else:
                parent_idx = (current_idx - 1) // 2

            parent_node = self.heap[parent_idx]

            if parent_node > num:
                self.heap[current_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[current_idx]
                current_idx = parent_idx
            else:
                break

    def sift_down(self):
        root_idx = 0
        root_value = self.heap[root_idx]

        while True:
            left_node_idx = root_idx * 2 + 1
            right_node_idx = root_idx * 2 + 2

            if left_node_idx >= len(self.heap):
                break

            elif right_node_idx >= len(self.heap):
                self.heap[root_idx], self.heap[left_node_idx] = self.heap[left_node_idx], self.heap[root_idx]
                return root_value
                        
            if self.heap[left_node_idx] < self.heap[right_node_idx]:
                self.heap[root_idx], self.heap[left_node_idx] = self.heap[left_node_idx], self.heap[root_idx]
                root_idx = left_node_idx
            else:
                self.heap[root_idx], self.heap[right_node_idx] = self.heap[right_node_idx], self.heap[root_idx]
                root_idx = right_node_idx

        last_node = self.heap[-1]
        self.heap[-1], self.heap[root_idx] = self.heap[root_idx], self.heap[-1]
        self.sift_up(last_node, root_idx)
        return root_value
            
    def get_min(self):
        return self.heap[0]
