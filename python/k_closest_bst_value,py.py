# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 01:43:01 2019

@author: shrey
"""

#Leetcode 272 Closest Binary search Tree Value 2: FOr a variable k,
#return a list of k closest element 

class Node:
    def __init__(self, data):  
        self.val = data  
        self.left = None
        self.right = None

def getPredecessor(root,key,pr):
    if root is None:
        return
    
    getPredecessor(root.left,key,pr)
    if root.val>key:
        return
    pr.append(root)
    getPredecessor(root.right,key,pr)
    
def getSuccessor(root,key,sr):
    if root is None:
        return
    
    getSuccessor(root.right,key,sr) 
    if root.val<=key:
        return
    sr.append(root)
    getSuccessor(root.left,key,sr) 

def k_closest_bst_value(root,key,k):
    if root is None:
        return []
    
    pr=[]
    sr=[]
    getPredecessor(root,key,pr)
    getSuccessor(root,key,sr)
    
    res=[]
    
    for i in range(k):
        if len(pr)==0:
            res.append(sr.pop().val)
        elif len(sr)==0:
            res.append(pr.pop().val)
        elif abs(key-pr[-1].val)>abs(key-sr[-1].val):
            res.append(sr.pop().val)
        else:
            res.append(pr.pop().val)
    
    return res

root=Node(9)
root.left=Node(4)
root.right=Node(17)
root.left.left=Node(3)
root.left.right=Node(6)
root.left.right.left=Node(5)
root.left.right.right=Node(7)
root.right.right=Node(22)
root.right.right.left=Node(20)

k=5
key=20

print(k_closest_bst_value(root,key,k))

    