#Made by Shade2go and Tiervisten
import random

operation_list = ["+", "-", "*"]

def math_question_generator():
    random_operation = random.choice(operation_list)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if random_operation == "+":
        answer = num1 + num2
    elif random_operation == "-":
        answer = num1 - num2
    elif random_operation == "*":
        answer = num1 * num2
    else:
        answer = None  # fallback, should never happen
    
    # Ask the user
    user_input = int(input(f"What is {num1} {random_operation} {num2}? "))
    if user_input == answer:
        print("Correct!")
        return 1
    else:
        print(f"Wrong! The correct answer is {answer}")
        return 0

score = 0
for i in range(10):
    score += math_question_generator()

print(f"\nYour final score is {score} out of 10.")
