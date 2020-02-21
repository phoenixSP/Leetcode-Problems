# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 07:04:24 2019

@author: shrey
"""

class Node:
    def __init__(self, data):  
        self.val = data  
        self.left = None
        self.right = None
        
def isBalanced(root, height):
    if root is None:
        return True
    l_height=[0]
    r_height=[0]
    lr=isBalanced(root.left,l_height)
    rr=isBalanced(root.right,r_height)
    
    height[0]=max(l_height[0],r_height[0])+1
    
    if abs(l_height[0]-r_height[0])>1:
        return False
    else:
        return lr and rr
    
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.right=Node(4)
#root.right.right.right=Node(5)
height=[0]
if isBalanced(root, height):
    print("True")
else:
    print("False")
    
    
#dct={1,2,3}
#q=1
#if q in dct:
#    print("Yes")