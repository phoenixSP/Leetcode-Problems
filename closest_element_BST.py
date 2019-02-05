# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:09:07 2019

@author: shrey
"""
#leetcode 270

class Node:
    def __init__(self, data):  
        self.key = data  
        self.left = None
        self.right = None

def closest_element_BST_util(node,key,diff,diff_key):
    if node is None:
        return
    #print(diff)
#    diff[0]=min(diff[0],abs(key-node.key))
#    print('diff',diff[0])
    if diff[0]>abs(key-node.key):
        diff[0]=abs(key-node.key)
        diff_key[0]=node.key
        print(diff_key[0])
        
    if diff[0]==0:
        return
    
    if key<node.key:
        closest_element_BST_util(node.left,key,diff, diff_key)
    else:
        closest_element_BST_util(node.right,key,diff, diff_key)
        
def closest_element_BST(root,key):
    diff=[]
    diff.append(99999)
    diff_key=[-1]
    closest_element_BST_util(root,key,diff,diff_key)
    print(diff[0], diff_key[0])
    
root=Node(9)
root.left=Node(4)
root.right=Node(17)
root.left.left=Node(3)
root.left.right=Node(6)
root.left.right.left=Node(5)
root.left.right.right=Node(7)
root.right.right=Node(22)
root.right.right.left=Node(20)

k=20

closest_element_BST(root,k)