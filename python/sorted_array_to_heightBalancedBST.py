# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 23:54:09 2019

@author: shrey
"""

# Leetcode 108 Convert Sorted Array to Binary Search Tree

class Node:
    def __init__(self,data):
        self.val=data
        self.left=self.right=None
        
def convert_minimalBST(array):
    if len(array)==0:
        return None
    
#    if len(array)%2!=0:
#        mid=int(0.5*len(array))
#    else:
#        mid=int(0.5*len(array)-1)
        
    mid=(len(array)-1)//2
        
    node=Node(array[mid])
    node.left=convert_minimalBST(array[:mid])
    node.right=convert_minimalBST(array[mid+1:])
    return node

def inorder(root): 
        if root: 
            inorder(root.left) 
            print(root.val) 
            inorder(root.right) 
            
            
array=[1,2,3,4,5,6,7]
root=convert_minimalBST(array)
print(root.val)
inorder(root)

    