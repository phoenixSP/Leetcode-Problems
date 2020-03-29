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
            if max_len < curr_len:
                max_len = curr_len 
            
        return max_len
                        
        
        
#two pointer method
        d = {}
        p1 = p2 = m = 0
        
        while p2 < len(s):
            if s[p2] not in d:
                d[s[p2]] = True
                p2 += 1
                m = max(len(d), m)
            else:
                del d[s[p1]]
                p1 += 1
                            
        return m
                