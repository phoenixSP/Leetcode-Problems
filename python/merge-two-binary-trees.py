# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:11:15 2020

@author: shrey
"""

def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    
    if t1 is None:
        return t2
    
    if t2 is None:
        return t1
    
    t1.val += t2.val
    t1.left = self.mergeTrees(t1.left, t2.left)
    t1.right = self.mergeTrees(t1.right, t2.right)
    
    return t1