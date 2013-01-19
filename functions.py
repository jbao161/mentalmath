'''
Created on Jan 3, 2013
Computes solutions to arithmetic problems
@author: jbao
'''
def product(input_set,rounding): # multiplies all the numbers in the input_set        
    result=1
    for number in input_set:
        result=result*number
    return result

def add(input_set,rounding): # adds all the numbers in the input_set
    result=0
    for number in input_set:
        result+=number
    return result

def divide(input_set,rounding): # first number in the input_set divided by each other number 
    # note: returns a decimal value. not practical for checking answers!
    result = 0.0+input_set[0]**2
    for number in input_set:
        result=result/number
    return round(result,rounding)

def subtract(input_set,rounding): # first number in the input_set minus each other number 
    result = input_set[0]*2
    for number in input_set:
        result=result-number
    return result