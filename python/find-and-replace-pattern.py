# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:04:29 2020

@author: shrey
"""

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def getCount(word):
            curr = 0
            chars = []
            string = ""
            
            for char in word:
                if char not in chars:
                    chars.append(char)
                string += str(chars.index(char))

            return string
            
        pattern_cnt_array = getCount(pattern)
        res = []
        for word in words:
            if getCount(word) == pattern_cnt_array:
                res.append(word)
                
        return res