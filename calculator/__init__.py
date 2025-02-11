from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    """A Calculator class that uses Calculation objects for operations."""

    @staticmethod
    def _perform_operation(a, b, operation):
        """Helper function to avoid repeating the same logic."""
        calculation = Calculation(a, b, operation)
        return calculation.get_result()

    @staticmethod
    def add(a, b):
        """Perform addition and return result."""
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a, b):
        """Perform subtraction and return result."""
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a, b):
        """Perform multiplication and return result."""
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a, b):
        """Perform division and return result. Raises exception for division by zero."""
        return Calculator._perform_operation(a, b, divide)
