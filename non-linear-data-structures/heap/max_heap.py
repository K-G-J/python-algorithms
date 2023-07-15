"""
In a MaxHeap, parent nodes should always be larger than their children, and the root node is the maximum element. This is in contrast to a MinHeap where parent nodes are smaller than their children and the root node is the minimum element.

In the heapify_up method, check if the parent node is smaller than the child, instead of greater, and in the heapify_down method, check if the parent node is smaller than the largest child, instead of greater than the smallest child.

This code will create a MaxHeap instead of a MinHeap. It still maintains a binary tree structure where each parent node is greater than its children. The heapify_up and heapify_down methods ensure the heap property is maintained after an element is added or the maximum element is removed.
"""


class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    def retrieve_max(self):
        if self.count == 0:
            print("No items in heap")
            return None

        max = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        self.heapify_down()
        return max

    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def get_larger_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child > right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)

    def heapify_up(self):
        idx = self.count
        swap_count = 0
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)] < self.heap_list[idx]:
                swap_count += 1
                tmp = self.heap_list[self.parent_idx(idx)]
                self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = self.parent_idx(idx)

        element_count = len(self.heap_list)
        if element_count > 10000:
            print("Heap of {0} elements restored with {1} swaps"
                  .format(element_count, swap_count))
            print("")

    def heapify_down(self):
        idx = 1
        swap_count = 1
        while self.child_present(idx):
            larger_child_idx = self.get_larger_child_idx(idx)
            if self.heap_list[idx] < self.heap_list[larger_child_idx]:
                swap_count += 1
                tmp = self.heap_list[larger_child_idx]
                self.heap_list[larger_child_idx] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = larger_child_idx

        element_count = len(self.heap_list)
        if element_count >= 10000:
            print("Heap of {0} elements restored with {1} swaps"
                  .format(element_count, swap_count))
            print("")
