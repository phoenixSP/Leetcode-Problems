# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:50:02 2020

@author: shrey
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0 or len(s)==1:
            return len(s)
        
        chars = {}
        curr_len = 0
        max_len = 0
        for i, ch in enumerate(s):
            if ch in chars:
                curr_len = i - chars[ch]
                chars = {k:v for k,v in chars.items() if v > chars[ch] }
                
            else:
                curr_len += 1
                
            chars[ch] = i
            max_len = max( max_len, curr_len)
            
        return max_len
                        
        
        
#two pointer method
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # experiment was performed by changing the charset from dictionary to list
        # the average time complexity for deleting an element from a list is O(n) while it is O(1) for a dictionary
        
        charset = {}
        
        start = end = length = 0
        
        while end < len(s):
            
            if s[end] not in charset:
                charset[s[end]] = True
                end += 1
                length = max(length, len(charset))
            else:
                del charset[s[start]]
                start += 1
                
        return length
                
