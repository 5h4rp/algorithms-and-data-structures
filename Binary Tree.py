# Implementation of a binary tree
# left node smaller than the data and right is bigger


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if (value <= self.data):
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value < data:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right == None:
                return None
            else:
                return self.right.contains(value)

    def printInOrder(self):
        if self.left != None:
            self.left.printInOrder()
        print(self.data)
        if self.right != None:
            self.right.printInOrder()

# dfs returns a tuple with the diameter and depth of the tree

    def dfs(self):
        if self.left == None:
            left = (0, 0)
        else:
            left = self.left.dfs()
        if self.right == None:
            right = (0, 0)
        else:
            right = self.right.dfs()
        diam = max(left[0], right[0], left[1] + right[1])
        return (diam, max(left[1], right[1]) + 1)


testTree = Node(10)
testTree.insert(5)
testTree.insert(15)
testTree.insert(8)

testTree.printInOrder()
print(testTree.dfs())
