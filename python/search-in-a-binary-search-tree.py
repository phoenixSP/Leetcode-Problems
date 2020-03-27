# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:11:28 2020

@author: shrey
"""

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            return None
        
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)