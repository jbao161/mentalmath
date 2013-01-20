mentalmath
==========
             Asks the user to solve random arithmetic problems (+,x,-,/)
             And analyzes user speed and accuracy.

mental_math 

             (number of problems, 
             how many numbers in each problem, 
             how many digits in each number, 
             operation)
             
             possible entries for operation are: 'multiply', 'add', 'subtract', 'divide'
             (note: checking answers for division is not practical!)

Examples:
             
             mental_math(1,2,3,'subtract')
             --> 379 - 244 = 
             mental_math(2,2,2,'multiply')
             --> 79 x 44 = 
                 19 x 75 = 

Example execution:
             mental_math(5,2,2,'multiply')
             
             Would you like to log your responses? y/n n
             99 x 11 = 1089
             77 x 65 = 5005
             27 x 62 = 1674
             24 x 82 = 1968
             48 x 42 = 2016
             
             Correct answers 5 out of 5 total. Accuracy: 1.0
             Response time (seconds): avg = 39.06. max = 65.3. min = 21.22
             
             99 x 11 = 1089. You answered "1089" in 21.62 seconds. You were correct!
             77 x 65 = 5005. You answered "5005" in 65.3 seconds. You were correct!
             27 x 62 = 1674. You answered "1674" in 45.29 seconds. You were correct!
             24 x 82 = 1968. You answered "1968" in 21.22 seconds. You were correct!
             48 x 42 = 2016. You answered "2016" in 41.84 seconds. You were correct!
    
@author: jbao
