# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:51:31 2020

@author: shrey
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        this_level = [root]
        next_level = []
        
        while this_level:
                node = this_level.pop(0)
                    
                if node.left:
                    next_level.append(node.left)
                    
                if node.right:
                    next_level.append(node.right)
                    
                if not this_level:
                    node.next = None
                    this_level = next_level
                    next_level = []
                else:
                    node.next = this_level[0]
                                    
        return root
    
    
    #optimized code: O(1) memory
    
    
    