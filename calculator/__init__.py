"""
Basic calculator module that provides arithmetic operations.
"""

def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Returns the difference between two numbers.
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of two numbers.
    """
    return a * b

def divide(a, b):
    """
    Returns the result of dividing the first number by the second.
    Raises a ValueError if the second number is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
