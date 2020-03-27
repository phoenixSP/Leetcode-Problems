# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 12:33:26 2020

@author: shrey
"""

class Solution:
    def __init__(self):
        self.res = []
        
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        
        self.res.append(root.val)
        
        
        for ch in root.children:
            self.preorder(ch)
        
        return self.res
        