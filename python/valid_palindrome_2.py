# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:04:16 2019

@author: shrey
"""

'''
problem number 680. Valid Palindrome II

'''

def validPalindrome(s):
    start = 0
    end = len(s) - 1 
    while start < end: 
        if s[start] != s[end]:
            print('one', s[start:end+1])
            return isPalindrome(s,start+1, end) or isPalindrome(s,start,end-1)
        else:
            start += 1
            end -= 1
    return True

def isPalindrome(string, start, end):
    substring = string[start:end+1]
    if substring == substring[::-1]:
        return True
    return False

x = validPalindrome('abcxxa')