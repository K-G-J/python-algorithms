import random

"""
BinarySearchTree class containing value, depth, and left and right child nodes.

An .insert() method to place a node of a specified value at the correct location in the Binary Search Tree. The time efficiency of this operation is O(logN) for a balanced tree - if there are N nodes in the BST, the max depth of a balanced tree is log(N). So, this method makes at most log(N) value comparisons. In the worst case of an imbalanced tree (all values on one side), the performance would be O(N).

A .get_node_by_value() method to retrieve a node in the tree by its value. The time efficiency of this operation is also O(logN) for a balanced tree - if there are N nodes in the BST, the max depth of the tree is log(N), so this method makes at most log(N) value comparisons. In the worst case of an imbalanced tree (all values on one side), the performance would be O(N).

A .depth_first_traversal() method to print the inorder traversal of the Binary Search Tree. This visits every single node, so if there are N nodes, the time efficiency for traversal is O(N).
"""


class BinarySearchTree:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if (value < self.value):
            if (self.left is None):
                self.left = BinarySearchTree(value, self.depth + 1)
                print(
                    f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
        else:
            if (self.right is None):
                self.right = BinarySearchTree(value, self.depth + 1)
                print(
                    f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        if (self.value == value):
            return self
        elif ((self.left is not None) and (value < self.value)):
            return self.left.get_node_by_value(value)
        elif ((self.right is not None) and (value >= self.value)):
            return self.right.get_node_by_value(value)
        else:
            return None

    def depth_first_traversal(self):
        if (self.left is not None):
            self.left.depth_first_traversal()
        print(f'Depth={self.depth}, Value={self.value}')
        if (self.right is not None):
            self.right.depth_first_traversal()


print("Creating Binary Search Tree rooted at value 15:")
tree = BinarySearchTree(15)

for x in range(10):
    tree.insert(random.randint(0, 100))

print("Printing the inorder depth-first traversal:")
tree.depth_first_traversal()
