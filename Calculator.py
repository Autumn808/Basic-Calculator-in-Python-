"""Autumn Capasso
UMUC SDEV 300
Oct 23, 2019
Python Calculator Program
This program can add, subtract, multiply, divide, and modulos
"""

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
def add(x, y):
    return x + y


# Subtraction Function
def sub(x, y):
    return x - y


# Multiplication Function
def multiply(x, y):
    return x * y


# Divide Function
def divide(x, y):
    return x / y


# Modulus Function
def modulus(x, y):
    return x % y


# Exit Function
def end_program():
    exit()


# User Input for Selection

selection = input("Enter selection: ")

if selection >= '6':
    print('Invalid input')
    print('Thank you for trying the calculator program', end_program())

Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))

if selection == '1':
    print(Num1, "+", Num2, "=", add(Num1, Num2))
    print('Thank you for trying the calculator program')

if selection == '2':
    print(Num1, "-", Num2, "=", sub(Num1, Num2))
    print('Thank you for trying the calculator program')

if selection == '3':
    print(Num1, "*", Num2, "=", multiply(Num1, Num2))
    print('Thank you for trying the  calculator program')

if selection == '4':

    if Num2 != 0:
        print(Num1, "/", Num2, "=", divide(Num1, Num2))
        print('Thank you trying the calculator program')

    if Num2 == 0:
        print("Invalid input")

if selection == '5':
    print(Num1, "%", Num2, "=", modulus(Num1, Num2))
    print('Thank you for trying to calculator program')
