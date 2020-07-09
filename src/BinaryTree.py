# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 08:28:33 2020

@author: Manish
"""


class Node:
    """Implementing the class Node for usage in BinaryTree."""

    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree():
    """
    I implemented a binary tree for practice.

    In a binary tree, nodes to the right of a given node are greater while
    those to the left are smaller.
    """

    def __init__(self):
        self.rootNode = None
        self.no_of_Nodes = 0

    def insert(self, val):
        """Will insert a node into the binary tree."""
        try:
            float(val)
        except ValueError:
            print("Not a number")
            return False
        self.no_of_Nodes += 1
        if self.rootNode is None:
            self.rootNode = Node(val)
            return True

        currentNode = self.rootNode
        while True:
            if currentNode.val < val:
                if currentNode.right is None:
                    currentNode.right = Node(val)
                    currentNode.right.parent = currentNode
                    return True
                else:
                    currentNode = currentNode.right
            else:
                if currentNode.left is None:
                    currentNode.left = Node(val)
                    currentNode.left.parent = currentNode
                    return True
                else:
                    currentNode = currentNode.left

    def insert_arr(self, val_arr=[]):
        """Will add an array of values into the binary tree."""
        for x in val_arr:
            self.insert(x)

    def display_tree(self, tree_node, spacing=""):
        """
        display_tree displays the binary tree.

        Ways to improve function :
        1. At present it implements recursion. I want to try and implement
        iteration instead.
        2. Also, the display is unintutive. Will try to beautify the display
        with arrows.
        """
        if tree_node is None:
            return
        else:
            print(spacing + str(tree_node.val))
            spacing += "  "
            self.display_tree(tree_node.left, spacing)
            self.display_tree(tree_node.right, spacing)
