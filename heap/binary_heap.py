def max_comparator(a, b):
    return a > b

def min_comparator(a, b):
    return a < b

'''
By default it uses the min_comparator to create a min heap with an initial capacity of 9.
'''
class BinaryHeap:

    def __init__(self, capacity=9, comparator=min_comparator):
        self.size = 0
        self.capacity = capacity
        self.heap = [-1] * capacity
        self.comparator = comparator

    def heapify_up(self, index):
        if index <= 0:
            return
        parent_index = self.get_parent_index(index)
        if self.comparator(self.heap[index], self.heap[parent_index]):
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self.heapify_up(parent_index)

    def insert(self, value):
        if self.size == self.capacity:
            raise Exception('Heap overflow')
        self.heap[self.size] = value
        self.size += 1
        self.heapify_up(self.size - 1)
        return True

    def peak(self):
        if self.size == 0:
            raise Exception('Heap is empty')
        return self.heap[0]

    def heapify_down(self, index):
        if index >= self.size:
            return
        smallest_index = -1
        left_child_index = self.get_left_child_index(index)
        if 0 < left_child_index < self.size:
            smallest_index = left_child_index
            right_child_index = self.get_right_child_index(index)
            if right_child_index > 0 and self.comparator(self.heap[right_child_index], self.heap[left_child_index]):
                smallest_index = right_child_index
        if smallest_index >= 0:
            self.heap[smallest_index], self.heap[index] = self.heap[index], self.heap[smallest_index]
            self.heapify_down(smallest_index)

    def poll(self):
        if self.size == 0:
            raise Exception('Heap is empty')
        min_value = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify_down(0)
        return min_value

    def get_capacity(self):
        return self.capacity

    def get_size(self):
        return self.size

    def get_parent_index(self, child_index):
        if child_index <= 0 or child_index >= self.size:
            return -1
        return (child_index - 1) // 2

    def get_left_child_index(self, parent_index):
        if self.size == 0:
            return -1
        return 2 * parent_index + 1

    def get_right_child_index(self, parent_index):
        if self.size == 0:
            return -1
        return 2 * parent_index + 2

    def print_heap(self):
        print('[ ', end='')
        for i in range(self.size):
            print(self.heap[i], end=' ')
        print(']')

if __name__ == '__main__':
    # heap = BinaryHeap(comparator=max_comparator)
    heap = BinaryHeap(capacity=6)
    heap.insert(5)
    heap.insert(4)
    heap.insert(7)
    heap.insert(8)
    heap.insert(1)
    heap.insert(3)
    print("Popped element: ", heap.poll())
    heap.print_heap()