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

    def is_leaf_node(self):
        """Returns True if the node is a leaf node(i.e. no children)."""
        if self is None:
            return False
        if self.left is None and self.right is None:
            return True
        return False

    def node_type(self):
        if self is None:
            return "None"  # Empty
        if self.parent is None:
            return "Root"  # Root Node
        if self.parent.val< self.val: 
            return "Right" # Right node (as larger numbers to right).
        else:
            return "Left"

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

    def search(self, val):
        """Searches number in binary tree."""
        currentNode = self.rootNode
        while True:
            if currentNode is None:
                print("Number not found.")
                return None
            elif currentNode.val == val:
                print("Number found.")
                return currentNode
            elif currentNode.val < val:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left

    def delete(self, val):
        """
        Deletes number from binary tree.
        
        This function hasn't been implemented for case 3.
        Clearly iteration isn't the way to go for binary search trees.
        The code is a horror to look at :(
        I have to find the inorder successor to this code now. Do deletion of
        inorder successor in a while loop.
        Write function for that and then, ultimately do a while loop to carry out deletion.
        Obviously a loop is needed as deletion is a log(N) operation. Therefore, I have
        to re-write everything with a loop! :(
        """
        # We will be searching the bianry tree for the value.
        del_node = self.search(val)  # Node to be deleted.
        if del_node is None:  # This means that the value wasn't found.
            return False  # Deletion not done
        # Case 1: Leaf Node is being deleted (the simplest case).
        elif del_node.is_leaf_node() is True:
            if del_node.node_type() == "Left":
                del_node.parent.left = None
            elif del_node.node_type == "Right": 
                del_node.parent.left = None
            else:
                print("Weird bug in delete, God help us!")
            return True  # Deletion done
            del(del_node)
        # Case 2: Node with one child
        elif del_node.left is None or del_node.right is None:
            store_node = None
            if del_node.left is None:
                store_node = del_node.right
            else:
                store_node = del_node.left

            if del_node.node_type() == "Root":
                self.rootNode = store_node
                del(del_node)
            elif del_node.node_type() == "Left":
                del_node.parent.left = store_node
                del(del_node)
            elif del_node.node_type() == "Right":
                del_node.parent.right = store_node
                del(del_node)
            else:
                print("Weird bug 2 in delete, God help us!")
        # Case 3: Node with 2 children
        
        