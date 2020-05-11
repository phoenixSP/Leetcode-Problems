# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:53:42 2020

@author: shrey
"""


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        wordDict = {}
        
        for word in words:
            if word in wordDict:
                wordDict[word] += 1
                
            else:
                wordDict[word] = 1
                
        res = sorted(wordDict, key=lambda x: (-wordDict[x], x))
        return res[:k]
                