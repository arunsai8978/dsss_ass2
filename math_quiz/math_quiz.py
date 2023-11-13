import random


# A function to randomly select a number from two integers between min and max numbers
def random_number(min, max):
    """
    min: minimun number
    max: Maximum number
    """
    return random.randint(min, max)

# A function to randomly select an operator among {"+","-","*"}
def random_operator():
    return random.choice(['+', '-', '*'])

# A function to perform math operations and returns the problem and solution
def math_operation(first_num, second_num, operator):
    """
    first_num = initialized first number
    second_num = intialized second number
    operator = randomly selected an operator
    """
    problem = f"{first_num} {operator} {second_num}"
    if operator == '+': solution = first_num + second_num
    elif operator == '-': solution = first_num - second_num
    else: solution = first_num * second_num
    return problem, solution

# A function to start the math quiz
def math_quiz():
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        first_num = random_number(1, 10); second_num = random_number(1, 5); operator = random_operator()

        PROBLEM, ANSWER = math_operation(first_num, second_num, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        try :
            useranswer = int(useranswer)
        except:
            print(f"invalid_input : please enter an integer")
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
