# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:06:12 2020

@author: shrey
"""
from collections import defaultdict

# Employee info
'''
class Employee:
    def __init__(self, emp_id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.emp_id = emp_id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, emp_id):
        
        importance = {}
        graph = defaultdict(lambda: [])
        
        for employee in employees:
            importance[employee.emp_id] = employee.importance
            graph[employee.emp_id] += employee.subordinates
            
        print('importance', importance)   
        print('graph',graph)
        
        stack = [emp_id]
        imp = 0
        
        while len(stack)>0:
            emp_id = stack.pop()
            imp += importance[emp_id]
            
            stack += graph[emp_id]
            
        return imp
    
s1 = Solution()
e1 = Employee(1,2,[2])
e2 = Employee(2,3,[])
print(s1.getImportance([e1, e2], 2))
'''

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        #iterative solution
        importance = {}
        graph = defaultdict(lambda: [])
        
        for employee in employees:
            importance[employee.id] = employee.importance
            graph[employee.id] += employee.subordinates
        print(importance)   
        print(graph)
        stack = [id]
        imp = 0
        
        while len(stack)>0:
            _id = stack.pop()
            imp += importance[_id]
            
            stack += graph[_id]
            
        return imp
    
        #recursive solution
        def helper(employee_dict, id):
            emp = employee_dict[id]
            return emp.importance + sum([helper(employee_dict, sub) for sub in emp.subordinates])
            
        employee_dict = {emp.id: emp for emp in employees}
        return helper(employee_dict, id)
