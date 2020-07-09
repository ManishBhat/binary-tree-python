# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:03:45 2020

@author: Manish
"""

from src.BinaryTree import BinaryTree

a = BinaryTree()

print("TESTING INSERTION")
#a.insert_arr([6, 4, 7, 1, 5, 2, 1.5, 3, 4.5, 5.5, 9, 8, 10])
a.insert_arr([6, 4, 7, 1, 5, 2, 1.5, 3, 4.5, 5.5, 9, 11, 10])
a.display_tree(a.rootNode)
print()

print("TESTING SEARCH")
mynode = a.search(10)
print(mynode.parent.val)
print()

print("TESTING DELETION")
a.delete(4.5)
a.display_tree(a.rootNode)

a.delete(9)
a.display_tree(a.rootNode)
