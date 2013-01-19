'''
Created on Jan 3, 2013
Analyzes the speed and accuracy of user's response.
@author: jbao
'''
def avg_timing(response_sheet,rounding): # returns average time user took to respond
    total=0.0
    count=len(response_sheet)
    for response in response_sheet:
        total+=response[3]
    return round(total/count,rounding)

def extrem_timing(response_sheet,rounding): # returns [max, min] time user took to respond
    maximum=0.0
    minimum=response_sheet[0][3]
    for response in response_sheet:
        if response[3]>maximum:
            maximum = response[3]
        if response[3]<minimum:
            minimum = response[3]
    return [round(maximum,rounding),round(minimum,rounding)]

def calculate_score(response_sheet,rounding): # returns [correct,total,percentage] answers
    score=0
    total=len(response_sheet)
    for response in response_sheet:
        if response[2]:
            score+=1
    return [score,total,round(1.0*score/total,rounding)]
