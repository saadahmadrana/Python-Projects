import math
import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."

def exponentiate(base, exp):
    return base ** exp

def square_root(x):
    if x < 0:
        return "Error: Cannot compute the square root of a negative number."
    return math.sqrt(x)

def sine(angle):
    return round(math.sin(math.radians(angle)), 2)

def cosine(angle):
    return round(math.cos(math.radians(angle)), 2)

def tangent(angle):
    return round(math.tan(math.radians(angle)), 2)

def cotangent(angle):
    try:
        return round(1 / math.tan(math.radians(angle)), 2)
    except ZeroDivisionError:
        return "Error: Cotangent is undefined for this angle."

def secant(angle):
    try:
        return round(1 / math.cos(math.radians(angle)), 2)
    except ZeroDivisionError:
        return "Error: Secant is undefined for this angle."

def cosecant(angle):
    try:
        return round(1 / math.sin(math.radians(angle)), 2)
    except ZeroDivisionError:
        return "Error: Cosecant is undefined for this angle."

def natural_log(x):
    if x <= 0:
        return "Error: Logarithm is undefined for non-positive values."
    return math.log(x)

def log_base10(x):
    if x <= 0:
        return "Error: Logarithm is undefined for non-positive values."
    return math.log10(x)

def factorial(x):
    if x < 0:
        return "Error: Factorial is undefined for negative numbers."
    if not isinstance(x, int):
        return "Error: Factorial is only defined for integers."
    return math.factorial(x)

def calculator():
    while True:
        print("\n--- Basic Scientific Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Square Root")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Cotangent")
        print("11. Secant")
        print("12. Cosecant")
        print("13. Natural Logarithm")
        print("14. Logarithm Base 10")
        print("15. Factorial")
        print("16. Exit")
        
        choice = input("Select an operation (1-16): ")
        
        if choice == '16':
            print("Exiting the calculator. Goodbye!")
            sys.exit()
        
        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
        
        if choice == '6':
            try:
                num = float(input("Enter the number: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
        
        if choice in ['7', '8', '9', '10', '11', '12']:
            try:
                angle = float(input("Enter the angle in degrees: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
        
        if choice in ['13', '14']:
            try:
                num = float(input("Enter the number: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
        
        if choice == '15':
            try:
                num = int(input("Enter a non-negative integer: "))
            except ValueError:
                print("Invalid input. Please enter an integer value.")
                continue
        
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {exponentiate(num1, num2)}")
        elif choice == '6':
            print(f"Result: {square_root(num)}")
        elif choice == '7':
            print(f"Result: {sine(angle)}")
        elif choice == '8':
            print(f"Result: {cosine(angle)}")
        elif choice == '9':
            print(f"Result: {tangent(angle)}")
        elif choice == '10':
            print(f"Result: {cotangent(angle)}")
        elif choice == '11':
            print(f"Result: {secant(angle)}")
        elif choice == '12':
            print(f"Result: {cosecant(angle)}")
        elif choice == '13':
            print(f"Result: {natural_log(num)}")
        elif choice == '14':
            print(f"Result: {log_base10(num)}")
        elif choice == '15':
            print(f"Result: {factorial(num)}")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator()
