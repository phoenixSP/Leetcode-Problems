# -*- coding: utf-8 -*-
"""
Created on Sat May 23 18:35:33 2020

@author: shrey
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def boundaryTraversal(self, root):
        '''
        return: List
        '''
        #get left path, bottom path and right path
        
        res = []
        def getLeft(node):
            while node and (node.left or node.right):
                res.append(node.val)
                node = node.left
        getLeft(root)
        
        def getLeaves(node):
            if not node:
                return
            
            if not node.left and not node.right:
                res.append(node.val)
            
            getLeaves(node.left)
            getLeaves(node.right)
            
        getLeaves(root)
        
        def getRight(node):
            if not node:
                return
            
            getRight(node.right)
            res.append(node.val)
        
        getRight(root)
        return res[:-1]
                
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)

s = Solution()
x = s.boundaryTraversal(root)
print(x)
        