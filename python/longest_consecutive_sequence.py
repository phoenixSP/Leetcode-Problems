# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 17:16:00 2019

@author: shrey
"""
#leecode 128

def longest_concecutive_sequence(array):
    s=set()
    for item in array:
        s.add(item)
    res=0
    for index, item in enumerate(array):
        if item-1 not in s:
            while item in s:
                item+=1
            res=max(res,item-array[index])
    return res


array=[2,4,15,3,5,21, 65, 66,67,68]
print(longest_concecutive_sequence(array))   
        