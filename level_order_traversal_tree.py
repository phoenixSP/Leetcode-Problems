# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:37:06 2019

@author: shrey
"""

#leetcode 102 Binary Tree Level Order Traversal return a list containing lists
#of every node in the particular level

class Node:
    def __init__(self, data):  
        self.val = data  
        self.left = None
        self.right = None

def levelOrder(root):
    if root is None:
        print("Empty tree")
        return
        
    res=[]
    queue=[]
    queue.append(root)
    height=0
    
    while len(queue)>0:
        node_count=len(queue)
        level_queue=[]
        height+=1
        
        while node_count>0:
            node=queue.pop(0)
            level_queue.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            node_count-=1
        res.append(level_queue)
        
    print(res)
    print(height)
    
root=Node(9)
root.left=Node(4)
root.right=Node(17)
root.left.left=Node(3)
root.left.right=Node(6)
root.left.right.left=Node(5)
root.left.right.right=Node(7)
root.right.right=Node(22)
root.right.right.left=Node(20)

levelOrder(root)
    
        

    