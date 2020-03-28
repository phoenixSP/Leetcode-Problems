# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:33:22 2020

@author: shrey
"""

class Solution:
        
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        if len(root.children) == 0:
            return 1
        
        return 1 + max( [self.maxDepth(child) for child in root.children])