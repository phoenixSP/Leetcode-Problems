# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:57:01 2020

@author: shrey
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        if left is None and right is None:
            return None
        
        if left is None:
            return right
        else:
            return left