# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 23:55:04 2019

@author: shrey
"""

#leetcode 104 Maximum Depth of Binary Tree

class Node:
    def __init__(self, data):  
        self.val = data  
        self.left = None
        self.right = None

#def height_recursive(root):
#    if root is None:
#        return 0
#    
#    l_height=height_recursive(root.left)
#    r_height=height_recursive(root.right)
#    
#    return max(l_height,r_height)+1


def height_recursive(root, height):
    if root is None:
        return
    l_height=[0]
    r_height=[0]
    height_recursive(root.left,l_height)
    height_recursive(root.right,r_height)
    
    height[0]= max(l_height[0],r_height[0])+1

root=Node(9)
root.left=Node(4)
root.right=Node(17)
root.left.left=Node(3)
root.left.right=Node(6)
root.left.right.left=Node(5)
root.left.right.right=Node(7)
root.right.right=Node(22)
root.right.right.left=Node(20)

#root=Node(1)
#root.left=Node(2)
#root.right=Node(3)

height=[0]
height_recursive(root, height)
print(height[0])


