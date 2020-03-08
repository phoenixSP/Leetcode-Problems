# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:03:58 2020

@author: shrey
"""

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        curr = head
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return head