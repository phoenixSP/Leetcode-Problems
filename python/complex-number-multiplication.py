# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:23:00 2020

@author: shrey
"""

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        
        param1 = list(map(int, re.split('[+i]',a)[:2]))
        param2 = list(map(int, re.split('[+i]',b)[:2]))
        
        real = param1[0]*param2[0] - param1[1]*param2[1]
        im = param1[0]*param2[1] + param1[1]*param2[0]
        
        return str(real)+'+'+str(im)+'i'
    
        #much better method of doing
        
        ca, cb = [int(x) for x in a[:-1].split('+')], [int(x) for x in b[:-1].split('+')]
        cp = [str(ca[0]*cb[0] - ca[1]*cb[1]), str(ca[0]*cb[1] + ca[1]*cb[0])]
        return '+'.join(cp) + 'i'
    