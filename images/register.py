# calculator.py

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        return "Error: Division by zero!"
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == '+':
        print("Result:", add(x, y))
    elif op == '-':
        print("Result:", subtract(x, y))
    elif op == '*':
        print("Result:", multiply(x, y))
    elif op == '/':
        print("Result:", divide(x, y))
    else:
        print("Invalid operation!")
