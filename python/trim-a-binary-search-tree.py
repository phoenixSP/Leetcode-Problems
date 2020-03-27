# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 12:07:21 2020

@author: shrey
"""

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        '''
        if root is None:
            return root
        
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        
        if root.val < L:
            return root.right
        
        if root.val > R:
            return root.left
        
        return root
        
        '''
        if root is None:
            return root
        
        
        
        if root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        
        
            return root