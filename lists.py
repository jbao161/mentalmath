'''
Created on Jan 3, 2013
Creates list of random arithmetic problems for mentalmath program.

@author: jbao
'''
import random

def create_number(number_of_digits):
    if number_of_digits == 1:
        return random.randrange(1,10)
    
    # if the number of digits is two or more
    n=''
    n=n+str(random.randrange(1,10)) #leading digit cannot be zero
    if number_of_digits >=3:
        for index in range (1,number_of_digits-1):
            n=n+str(random.randrange(0,10))
    n=n+str(random.randrange(1,10)) #final digit cannot be zero
    return int(n)

# list of all the numbers contained in one problem
def create_input_set(number_in_each_input_set,number_of_digits):
    result=[]
    for index in range (0,number_in_each_input_set):
        result.append(create_number(number_of_digits))
    return result

# list of all the problems
def create_worksheet(number_of_input_sets, number_in_each_input_set, number_of_digits):
    result = []
    for index in range (0,number_of_input_sets):
        result.append(create_input_set(number_in_each_input_set,number_of_digits))
    return result

# list of all correct answers
def create_answer_sheet(response_sheet):
    result=[]
    for response in response_sheet:
        result.append(response[1])
    return result

# list of user response with their true/false value for whether they match correct answer
def create_response_only(response_sheet):
    result=[]
    for response in response_sheet:
        result.append([response[0],response[2]])
    return result