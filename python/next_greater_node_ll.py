# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:49:38 2019

@author: shrey
"""
#1019. Next Greater Node In Linked List

def nextLargerNodes(head):
    
    res = []
    stack = []
    
    while head:
        while stack and stack[-1][1] < head.val:
            res[stack.pop()[0]] = head.val
        stack.append([len(res), head.val])
        res.append(0)
        head = head.next
    return res