from math import floor, inf
"""
Functions that return the respectives member indexes
"""
def left_child(i):
    return 2*i


def right_child(i):
    return 2*i+1


def parent(i):
    return floor(i/2)


class Heap:
    def __init__(self, array=[]):
        self.heap = [None] + array
        self.__build_max_heap()

    """
    build_max_heap
    It takes just the non-leaves elements and heapify them.
    It works because we can say that all leaves are already
    max_heaps!
    @complexity Via simple analysis - O(n log n) 
                But, if we analyze it deeper, we can see that
                only the root node takes (log n) time. In general,
                we have that an element that is l levels above the
                leaves takes O(l). So, after some calculus, we have O(n).
    """
    def __build_max_heap(self):
        n = len(self.heap)
        for i in range(floor(n/2), 0, -1):
            self.max_heapify(i)

    """
    Heapify
    @params  i - element to start
    @complexity O(log n) [tree height]
    """
    def max_heapify(self, i):
        if left_child(i) < len(self.heap):
            left_value = self.heap[left_child(i)]

            right_value = -inf
            if right_child(i) < len(self.heap):
                right_value = self.heap[right_child(i)]
            
            if left_value > right_value:
                if self.heap[i] < left_value:
                    self.heap[i], self.heap[left_child(i)] =  self.heap[left_child(i)], self.heap[i]
                    self.max_heapify(left_child(i))
            else:
                if self.heap[i] < right_value:
                    self.heap[i], self.heap[right_child(i)] =  self.heap[right_child(i)], self.heap[i]
                    self.max_heapify(right_child(i))

    """
    Get Max
    It extracts the biggest value on heap, i.e, the root.
    @complexity O(1)
    """
    def get_max(self):
        return self.heap[1]

    """
    Extract Max
    It extracts the biggest value on heap, i.e, the root.
    After removing it (putting on the end of the array and pop),
    we use heapify at the new root to maintain the max_heap correct.
    @complexity O(log n) [tree height]
    """
    def extract_max(self):
        n = len(self.heap)
        max_value = self.heap[1]
        self.heap[1], self.heap[n-1] = self.heap[n-1], self.heap[1]
        self.heap.pop()
        self.max_heapify(1)
        
        return max_value

    """
    Heap-Sort
    Basically, the extract_max() do all the real job here.
    We only need to call it n times.
    @complexity O(n*log n)
    """
    def heapsort(self):
        output = []
        for i in range(1, len(self.heap)):
            output.append(self.extract_max())

        return output

    """
    Insert
    Uses bottom-up approach with increase_key()
    @complexity O(log n)
    """
    def insert(self, val):
        self.heap.append(val)
        self.__increase_key(len(self.heap) - 1)

    """
    Increase key (swift up)
    Checks (and swaps if necessary) if my parent is smaller than me
    @complexity O(log n)
    """
    def __increase_key(self, i):
        if i > 1 and i < len(self.heap):
            if self.heap[parent(i)] < self.heap[i]:
                self.heap[parent(i)], self.heap[i] = self.heap[i], self.heap[parent(i)]
                self.__increase_key(parent(i))