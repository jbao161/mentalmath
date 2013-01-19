mentalmath
==========
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
