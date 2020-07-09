# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:03:45 2020

@author: Manish
"""

from src.BinaryTree import BinaryTree

a = BinaryTree()
a.insert_arr([6,4,7,1,5,2,1.5,3,4.5,5.5,9,8,10])
a.display_tree(a.rootNode)