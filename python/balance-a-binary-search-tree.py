# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:52:08 2020

@author: shrey
"""

class Solution:
    def __init__(self):
        self.balanced_array = []
        
    def inorder(self, root):
            if root is None:
                return
            self.inorder(root.left)
            self.balanced_array.append(root.val)
            self.inorder(root.right)
            
    def array_to_bbst(self, array):
            if not array:
                return None
            
            mid = len(array)//2
            root = TreeNode(array[mid])
            root.left = self.array_to_bbst(array[:mid])
            root.right = self.array_to_bbst(array[mid+1:])
            
            return root
        
    def balanceBST(self, root: TreeNode) -> TreeNode: 
        self.inorder(root)
        return self.array_to_bbst(self.balanced_array)