"""
This module contains tests for the Calculation class.

The tests ensure that arithmetic operations using Calculation objects
return correct results and handle special cases like division by zero.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('2'), divide, Decimal('5'))
])
def test_calculation_operations(a, b, operation, expected):
    """Test calculation operations using the Calculation class."""
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    """Test the string representation (__repr__) of Calculation class."""
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match expected."
    
def test_divide_by_zero():
    """Ensure division by zero raises a ValueError."""
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
