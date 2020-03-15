# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:30:17 2020

@author: shrey
"""

class CustomStack:

    def __init__(self, maxSize: int):
        self.cstack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.cstack) < self.maxSize:
            self.cstack.append(x)

    def pop(self) -> int:
        if len(self.cstack) > 0:
            return self.cstack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if len(self.cstack) < k:
            self.cstack = [x + val for x in self.cstack]
        else:
            for i in range(k):
                self.cstack[i] += val
                
    def cprint(self):
        print(self.cstack)


# Your CustomStack object will be instantiated and called as such:
maxSize = 5
obj = CustomStack(5)
obj.push(2)
obj.cprint()
obj.push(3)
obj.cprint()
obj.push(4)
obj.cprint()
obj.push(5)
obj.cprint()
obj.push(6)
obj.cprint()
obj.push(7)
obj.cprint()
param_2 = obj.pop()
print(param_2)
obj.increment(3,3)
obj.cprint()