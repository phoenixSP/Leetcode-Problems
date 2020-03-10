# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:53:14 2020

@author: shrey
"""

def intToRoman(num: int):
    mapping = {1:'I',5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    
    digits = str(num)
    print(digits)
    
    roman = ""
    
    for i, d in enumerate(digits):
        print(i,d)
        d = int(d)
        
        tens = pow(10, len(digits) - i - 1)
        print(tens)
        if d == 4:
            roman += mapping[tens] + mapping[5*tens]
        elif d == 9:
            roman += mapping[tens] + mapping[10*tens]
        else:
            roman += int(d/5)*(mapping[5*tens] if int(d/5) > 0 else '') + d%5*mapping[tens]
            
    return roman

print(intToRoman(3999))