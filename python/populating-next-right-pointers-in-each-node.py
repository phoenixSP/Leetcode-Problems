# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:42:41 2020

@author: shrey
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        queue = [root]
        
        while len(queue) > 0:
            n = len(queue)
            print(n)
            
            for i in range(n):
                node = queue.pop(0)
                if i == n-1:
                    node.next = None
                else:
                    node.next = queue[0]
                    
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                                    
        return root