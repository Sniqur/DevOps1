# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from enum import Enum
def addition(number1, number2):
    result = number1 + number2
    return f"The result of addition two numbers is: {result}"

def substraction(number1, number2):
    result = number1 - number2
    return f"The result of substraction two numbers is: {result}"

def multiplication(number1, number2):
    result = number1 * number2
    return f"The result of multiplication two numbers is: {result}"

def division(number1, number2):
    try:
        result = number1 / number2
        return f"The result of division two numbers is: {result}"
    except:
        return "You can`t divide by 0"


print(""" Welcome to the Calculator Program! """)

#
num1 = float(input("Please enter the first number: "))
print()

num2 = float(input("Please enter the second number: "))
print()

print("""
Please select an operation:

1. Addition
2. Subtraction
3. Multiplication
4. Division

""")

funcNum = int(input("Enter your choice (1-4): "))

#dictionary of functions

functions = {1: addition(num1, num2),
             2: substraction(num1, num2),
             3: multiplication(num1, num2),
             4: division(num1, num2)}


if funcNum in functions:
    print(functions[funcNum])
else:
    print("Enter something between 1 and 4")