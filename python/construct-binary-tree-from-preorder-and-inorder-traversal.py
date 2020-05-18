# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:47:29 2020

@author: shrey
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        inorder_map = {}
        
        for idx, element in enumerate(inorder):
            inorder_map[element] = idx
            
        def util(low, high):
            if low > high:
                return None
            
            val = preorder.pop(0)
            root = TreeNode(val)
            idx = inorder_map[val]
            
            root.left = util(low, idx - 1)
            root.right = util(idx+1, high)
            
            return root
        
        return util(0, len(inorder) - 1)