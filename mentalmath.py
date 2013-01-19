'''
Created on Jan 2, 2013

Asks the user to solve random arithmetic problems (+,x,-,/)
And analyzes user speed and accuracy.

mental_math (number of problems, 
             how many numbers in each problem, 
             how many digits in each number, 
             operation)
             
possible entries for operation are: 'multiply', 'add', 'subtract', 'divide'
(note: checking answers for division is not practical!)

ex: mental_math(1,2,3,'subtract')
--> 379 - 244 = 
ex: mental_math(2,2,2,'multiply')
--> 79 x 44 = 
    19 x 75 = 

example performance analysis:
--> Correct answers 0 out of 2 total. Accuracy: 0.0
    Response time (seconds): avg = 0.84. max = 1.42. min = 0.26
    Your answer: 1. Correct answer: 3476. You answered in 1.42 seconds. You were incorrect!
    Your answer: 1. Correct answer: 1425. You answered in 0.26 seconds. You were incorrect!
    
@author: jbao
'''

import lists
import display
import analysis

import os,sys

from time import time

# main execution procedure
def mental_math(number_of_input_sets,number_in_each_input_set,number_of_digits,operation):
    # would you like to log results?
    logresults = input('Would you like to log your responses? y/n')
    
    # arithmetic problems are set up
    worksheet=lists.create_worksheet(number_of_input_sets, number_in_each_input_set, number_of_digits)
    response_sheet=[]
    rounding=2 # number of decimal places in timing and accuracy
    
    # user is presented with arithmetic problems
    for input_set in worksheet: 
        starttime = time()
        problem=display.display_input_set(input_set,display.parse_operation(operation))
        response=input (problem) # ask user the question
        timetaken = time() - starttime # time the user's response
        a=display.function_operation(operation)(input_set,rounding) # compute the answer
        response_sheet.append([response,a,response==str(a),timetaken,problem]) #record the user's response, correct answer, whether user answered correctly, response time, and the problem
    
    # user's responses are analyzed
    score=analysis.calculate_score(response_sheet,rounding)
    timing = analysis.extrem_timing(response_sheet,rounding)
    
    # user's results are stored to file
    if logresults in ['y','Y','yes','Yes','YES']:
        dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
        logpath = os.path.join(dirname, "userlog.txt")
        f = open(logpath, 'a')
        logstring=display.response_sheet_tostring(response_sheet)
        f.write(logstring)
        f.close()
    
    # user's results are displayed
    print('')
    print("Correct answers "+str(score[0])+" out of "+str(score[1])+" total. Accuracy: "+str(score[2]))
    print("Response time (seconds): avg = "+str(analysis.avg_timing(response_sheet,rounding))+". max = "+str(timing[0])+". min = "+str(timing[1]))
    print('')
    #option=input(prompt='To see the correct answers or just results, please type "answers" or "results".')
    display.display_results(response_sheet,'answers')


    
mental_math(5,2,2,'multiply')
