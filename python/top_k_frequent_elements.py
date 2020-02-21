# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:06:54 2020

@author: shrey
"""

#top k frequent elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #dictopmary implementation
        from collections import defaultdict
        
        k_dict = defaultdict(lambda: 0)
        for num in nums:
            k_dict[num] += 1
            
        k_dict = sorted(k_dict.items(), key=lambda x: x[1], reverse= True)
        print(k_dict)
        
        res = []
        for x in k_dict[:k]:
            res.append(x[0])
        
        return res
    
    
        #counter implementation
        from collections import Counter  
        return [x[0] for x in Counter(nums).most_common(k)]
    
        #heap implementation
    
        from heapq import heapify, heappop, heappush, heappushpop, heapreplace
        from collections import defaultdict
        
        counter = defaultdict(lambda: 0)
    
        for ele in nums: 
            counter[ele] += 1
            
        minheap = []
        
        for key, val in counter.items():
            if len(minheap) < k:
                heappush(minheap, (val, key))
                
            elif val > minheap[0][0]:
                #same performance
                #heappushpop(minheap, (val, key))
                heapreplace(minheap, (val, key))
               
        return [x[1] for x in minheap]
