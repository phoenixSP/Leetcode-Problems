# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:47:12 2020

@author: shrey
"""

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        elements = set()
        
        def inorder(root):
            if root:
                inorder(root.left)
                elements.add(root.val)
                inorder(root.right)
        
        inorder(root)        
        
        if len(elements) == 1:
            return True
        else:
            return False
                