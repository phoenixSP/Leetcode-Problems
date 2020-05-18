# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:52:10 2020

@author: shrey
"""

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            if root.val == sum:
                return True
            else:
                return False
        
        if self.hasPathSum(root.left, sum - root.val):
            return True
        
        if self.hasPathSum(root.right, sum -root.val):
            return True
        
        return False