"""Autumn Capasso
UMUC SDEV 300
March 15, 2020
Lab 1 Python Calculator Program
This program can add, subtract, multiply, divide, and modulos
"""
import sys


def main():
    # Display Menu
    print('Welcome to the Calculator Program ')
    print('Select operation')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Modulus ')

    # Functions for Calculator

    # Addition Function


""" Will compute the addition of two values passed into the function  """


def add(x_value, y_value):
    return x_value + y_value


# Subtraction Function
""" Will compute the subtraction of two values passed into the function  """


def sub(x_value, y_value):
    return x_value - y_value


# Multiplication Function
""" Will compute the multiplication of two values passed into the function  """


def multiply(x_value, y_value):
    return x_value * y_value


# Divide Function
""" Will compute the division of two values passed into the function  """


def divide(x_value, y_value):
    return x_value / y_value


# Modulus Function
""" Will compute the modulus of two values passed into the function  """


def modulus(x_value, y_value):
    return x_value % y_value


# Exit Function
def end_program():
    sys.exit()


# User Input for Selection
SELECTION: int = int(input("Enter Selection: "))

if SELECTION >= 6:
    print('Invalid input')
    print('Thank you for trying the calculator program', end_program())

NUM1 = int(input("Enter first number: "))
NUM2 = int(input("Enter second number: "))

if SELECTION == 1:
    print(NUM1, "+", NUM2, "=", add(NUM1, NUM2))
    print('Thank you for trying the calculator program')

if SELECTION == 2:
    print(NUM1, "-", NUM2, "=", sub(NUM1, NUM2))
    print('Thank you for trying the calculator program')

if SELECTION == 3:
    print(NUM1, "*", NUM2, "=", multiply(NUM1, NUM2))
    print('Thank you for trying the  calculator program')

if SELECTION == 4:

    if NUM2 != 0:
        print(NUM1, "/", NUM2, "=", divide(NUM1, NUM2))
        print('Thank you trying the calculator program')

    if NUM2 == 0:
        print("Invalid input")

if SELECTION == 5:
    print(NUM1, "%", NUM2, "=", modulus(NUM1, NUM2))
    print('Thank you for trying to calculator program')

if __name__ == "__main__":
    main()
