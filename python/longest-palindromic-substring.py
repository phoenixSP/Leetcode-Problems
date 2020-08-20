# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 19:15:40 2020

@author: shrey
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Dynamic Programming solution: O(n2) time complexity, O(n2) memory
        # Algorithm: the logic is if a substring is palindrome, then substring
        # excluding the first and last characters also forms a palindrome, AND 
        # the first and last characters are the same. This means:
        # s[i: j+1] is a palindrome if s[i] == s[j] and palindrome(s[i+1:j-1]) is True
        
        max_length = 1
        start = 0
        string_length = len(s)
        
        table = [[False for x in range(string_length)] for y in range(string_length)]
        
        for i in range(string_length):
            table[i][i] = True
            
        for i in range(string_length - 1):
            if s[i] == s[i + 1]:
                table[i][i+1] = True
                max_length = 2
                start = i
        
        
        for k in range(3,string_length + 1):
            for i in range(string_length - k + 1):
                j = i + k - 1
                
                if table[i+1][j-1] and (s[i] == s[j]):
                    table[i][j] = True
                    
                    if k > max_length:
                        start = i
                        max_length = k

        return s[start: start + max_length]       