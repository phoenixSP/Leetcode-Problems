# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:58:06 2020

@author: shrey
"""

class Solution:
    def helper(self, root):
        if root is None:
            return 
        
        self.helper(root.left)
        root.left = None
        self.cur.right = root
        self.cur = root
        self.helper(root.right)
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        res = self.cur = TreeNode(None)
        self.helper(root)
        return res.right