# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 12:36:42 2020

@author: shrey
"""

class Solution:
    def __init__(self):
        self.res = []
    def postorder(self, root: 'Node') -> List[int]:

        if not root:
            return
        
        for ch in root.children:
            self.postorder(ch)
            
        self.res.append(root.val)
        
        return self.res