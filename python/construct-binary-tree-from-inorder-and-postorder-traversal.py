# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:55:45 2020

@author: shrey
"""

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        inorder_map = {}
        
        for idx, element in enumerate(inorder):
            inorder_map[element] = idx
            
        def util(low, high):
            
            if low > high:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)
            idx = inorder_map[root_val]
            
            root.right = util(idx+1, high)
            root.left = util(low, idx - 1)
            
            return root
        
        return util(0, len(inorder) -1)