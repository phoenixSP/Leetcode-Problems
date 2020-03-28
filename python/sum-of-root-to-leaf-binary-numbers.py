# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:47:08 2020

@author: shrey
"""

class Solution:
    
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        
        def helper(root, curr):
        
            if root is None:
                return 0
            
            curr = (curr << 1) + root.val
            
            if root.left is None and root.right is None:
                return curr
            
            return ((helper(root.left, curr)) + (helper(root.right, curr))) 
        
        return helper(root, 0)
        
        '''
        def dfs(curr, node):
            curr = (curr << 1) + node.val
            if not (node.left or node.right): return curr   # leaf node
            else: return (dfs(curr, node.left) if node.left else 0) + (dfs(curr, node.right) if node.right else 0)
            
        return dfs(0, root)
    '''
        