# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:41:37 2020

@author: shrey
"""

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        
        if root is None:
            return 
        
        res = []
        queue = [root]
        
        while len(queue) > 0:
            node_count = len(queue)
            level_queue = []
            
            while node_count > 0:
                node = queue.pop(0)
                level_queue.append(node.val)
                
                if node.left is not None:
                    queue.append(node.left)
                    
                if node.right is not None:
                    queue.append(node.right)
                    
                node_count -= 1
                
            res.append(level_queue)
            
        return res[::-1]