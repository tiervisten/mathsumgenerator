#made by shade2go and tiervisten
import math
import random  
import time     
print("Welcome") 

def sumMathQuestions():
    score = 0
    for i in range(10):  
        a = random.randint(1,100)
        b = random.randint(1,100)
        theAnswer = a + b
        question = int(input(f"What's {a} + {b}\n"))
        if question == theAnswer: 
            print("Correct")
            score += 1   
            print(f"Score = {score}") 
        else: 
            print("Wrong")
            
sumMathQuestions() 
