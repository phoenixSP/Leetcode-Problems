# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:16:21 2020

@author: shrey
"""

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next