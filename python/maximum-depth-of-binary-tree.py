# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:58:30 2020

@author: shrey
"""

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: 
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1