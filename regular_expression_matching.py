# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:15:13 2019

@author: shrey
"""
#Leetcode problem 10

def regular_expression_matching(text, pattern):
    #the matrix is of dimensions  text_length+1 x pattern_length+1
    m=len(text)+1
    n=len(pattern)+1
    
    T=[[False]*(len(pattern)+1) for _ in range(len(text)+1)]#*(len(pattern)+1)
    T[0][0]=True
    
    for i in range(2, n):
        if pattern[i-1]=="*":
            T[0][i]=T[0][i-2]
            
    for i in range(1,m):
        for j in range(1,n):
            if text[i-1]==pattern[j-1] or pattern[j-1]==".":
                T[i][j]=T[i-1][j-1]
            elif pattern[j-1]=="*":
                T[i][j]=T[i][j-2]
                if text[i-1]==pattern[j-2] or pattern[j-2]==".":
                    T[i][j]=T[i][j] or T[i-1][j] 
                    
            
    return T[-1][-1]
    
T=regular_expression_matching("aaa","ab*a*c*a")
if T is True:
    print("match")
else:
    print("no match")
