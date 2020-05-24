# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:38:27 2020

@author: shrey
"""

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return None
        
        res = []
        q = [root]
        
        f = 0
        while q:
            n = len(q)
            level = []
            
            while n:
                node = q.pop(0)
                
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)    
                n -= 1
            
            if f:
                res.append(level[::-1])
                f = 0
            else:
                res.append(level)
                f = 1
            
        return res