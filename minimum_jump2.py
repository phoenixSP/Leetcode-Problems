# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 17:14:57 2019

@author: shrey
"""

#leetcode 45 Jump Game 2

def minimum_jump(array):
    minimum_jump=[9999]*len(array)
    jump_index=[-1]*len(array)
    
    minimum_jump[0]=0    
    for i in range(1,len(array)):
        for j in range(i):
            if i-j<=array[j]:
                if minimum_jump[j]+1<minimum_jump[i]:
                    minimum_jump[i]=minimum_jump[j]+1
                    jump_index[i]=j
            
    print(minimum_jump)            
    print(minimum_jump[-1])
    
array=[2,3,1,1,2,4,2,0,1,1]
minimum_jump(array)
                
        
    