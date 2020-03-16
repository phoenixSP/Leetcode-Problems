# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:28:19 2020

@author: shrey
"""

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
#        #recursive approach
#        def helper(node, min_val, max_val):
#            if node is None:
#                return True
#            
#            if node.val < min_val or node.val > max_val:
#                return False
#            
#            return (helper(node.left, min_val, node.val - 1) and helper(node.right, node.val + 1, max_val)) 
#        
#        return helper(root, -float('inf'), float('inf'))
        
        #inorder traversal
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True