'''
Created on Jan 3, 2013
Displays text and interprets strings.
@author: jbao
'''
import functions

def display_input_set(input_set,operation): # displays the arithmetic problem
    # note: operation is a string, e.g. ' x '
    string=''
    for number in input_set:
        string+=str(number)+(operation)
    return string[:-(len(operation))]+' = ' # replaces last operation with equals sign

def display_results(response_sheet,option):
    if option == 'answers':
        for response in response_sheet:
            print(response[4]+str(response[1])+". You answered \""+response[0]+"\" in "+str(round(response[3],2))+" seconds. You were "+boolean_translate(response[2])+"!")
    if option == 'results':
        for response in response_sheet:
            print("Your answer: "+response[0]+". You answered in "+str(round(response[3],2))+" seconds. You were "+boolean_translate(response[2])+"!")
 
def response_sheet_tostring(response_sheet):
    result=''
    for response in response_sheet:
        result+=str(response)+'\n'
    return result
     
def boolean_translate(boolean):       
    if boolean:
        return 'correct' 
    return 'incorrect'

def parse_operation(operation):
    if operation == 'multiply':
        return (' x ')
    if operation == 'divide':
        return (' / ')
    if operation == 'add':
        return (' + ')
    if operation == 'subtract':
        return (' - ')

def function_operation(operation):
    if operation == 'multiply':
        return (functions.product)
    if operation == 'divide':
        return (functions.divide)
    if operation == 'add':
        return (functions.add)
    if operation == 'subtract':
        return (functions.subtract)       