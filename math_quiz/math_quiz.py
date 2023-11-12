import random

# creates a random Integer between the intervall of the input variables min and max
def createRandomInteger(min, max):
    """
    create a random integer between the values min and max

    Args:
        min (int): The minimal value of the random integer
        max (int): The maximal value of the random integer

    Returns:
        int: the random integer
    """

    # Check if the input has the correct type, if it is not an integer return 0
    try:
        random.randint(min, max)
    except TypeError:
        print("Use an Integer for the min and max values of the function: createRandomInteger.")
        return 0
    except ValueError:
        print("Use an Integer for the min and max values of the function: createRandomInteger.")
        return 0
    return random.randint(min, max)

# randomly selects an arithmetic operator
def randomArithmeticOperator():
    """
    randomly selects one of the operators +, -, *.

    Returns:
        string: randomly selected operator
    """
    # possible operators are: +, - and *
    return random.choice(['+', '-', '*'])

# receives two variables and an operator. Calculates variable1 operator variable2. Returns the equation and the result.
def calculate(variable1, variable2, operator):
    """
    calculates the equation: variable1 operator variable2

    Args: 
        variable1 (int): the first variable of the equation
        variable2 (int): the second variable of the equation
        operator (string): the operator of the equation
    
    Returns:
        string: the equation
        int: the result of the equation
    """
    # combines the input to from the equation
    equation = f"{variable1} {operator} {variable2}"
    # calulations
    if operator == '+': result = variable1 + variable2      # + operation
    elif operator == '-': result = variable1 - variable2    # - operation
    else: result = variable1 * variable2                    # * operation
    return equation, result

# generates a math quiz, which askes a defined amount of questions and awards points for the correct answer.
def math_quiz():
    """
    math quiz generator, which asks you equations and if they are correct you receive a point
    """
    # variable for the score
    score = 0
    # Number of calculations that are asked
    numberOfCalculations = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(numberOfCalculations):
        # creates the variables and the operator
        variable1 = createRandomInteger(1, 10); variable2 = createRandomInteger(1, 6); operator = randomArithmeticOperator()
        # do the calculations
        PROBLEM, ANSWER = calculate(variable1, variable2, operator)
        # ask the calculation
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)
        # check the answer and calculate the score
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
    # print the final score
    print(f"\nGame over! Your score is: {score}/{numberOfCalculations}")

if __name__ == "__main__":
    math_quiz()
