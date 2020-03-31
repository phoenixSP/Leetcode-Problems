# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:36:08 2020

@author: shrey
"""

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #without trie
        res = []
        products.sort()
        
        for i in range(1,len(searchWord)+1):
            word_list = [word for word in products if searchWord[:i] == word[:i]]
            
            if len(word_list) > 3:
                word_list = word_list[:3] #can sort individually here, but no significant impact
            res.append(word_list)
            
        return res
    
    