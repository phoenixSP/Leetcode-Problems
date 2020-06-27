# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:58:40 2020

@author: shrey
"""

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root