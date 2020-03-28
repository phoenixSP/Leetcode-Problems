# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:24:54 2020

@author: shrey
"""

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def leafSimilarUtil(root):
            if root is None:
                return []
            
            if root.left is None and root.right is None:
                return [root.val]
            
            res = []
            
                
            res += leafSimilarUtil(root.left)
            res += leafSimilarUtil(root.right)
            
            return res
        
        if leafSimilarUtil(root1) == leafSimilarUtil(root2):
            return True
        else:
            return False