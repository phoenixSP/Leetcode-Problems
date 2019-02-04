# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 18:42:12 2019

@author: shrey
"""

def longest_substring_2characters(string):
#    s=set()
#    length=0
#    res=0
#    for index, item in enumerate(string):
#        if item in s:
#            print("item in s")
#            length+=1
#            print("current length",length)
#        else:
#            if len(s)<2:
#                print("adding s")
#                s.add(item)
#                length+=1
#                print("current length",length)
#            else:
#                s.clear()
#                res=max(res,length)
#                length=0
#                
#    return max(res,length)
    
    
    s=dict()
    start=0
    res=0
    for index, item in enumerate(string):
        if item in s.keys():
            s[item]=index
        else:
            if len(s)<2:
                s[item]=index
            else:
                start=min(s.values())+1
                element=min(s.keys(), key=lambda x: s[x])
                s.pop(s[element], None) # check why it was previously giving key error 
                s[item]=index
        length=index-start+1
        res=max(length,res)
    return res
    
string="aeaebbc"
print(longest_substring_2characters(string))