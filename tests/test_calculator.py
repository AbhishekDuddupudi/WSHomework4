"""
This module contains tests for the Calculator class.

The tests verify that basic arithmetic operations (addition, subtraction, multiplication, division)
are correctly performed by the Calculator class.
"""

from decimal import Decimal
import pytest
from calculator import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (Decimal('10'), Decimal('5'), Decimal('15')),
    (Decimal('-2'), Decimal('2'), Decimal('0')),
    (Decimal('0'), Decimal('0'), Decimal('0'))
])
def test_add(a, b, expected):
    """Test the add function in Calculator class."""
    assert Calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (Decimal('10'), Decimal('5'), Decimal('5')),
    (Decimal('-2'), Decimal('-2'), Decimal('0')),
    (Decimal('0'), Decimal('5'), Decimal('-5'))
])
def test_subtract(a, b, expected):
    """Test the subtract function in Calculator class."""
    assert Calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (Decimal('10'), Decimal('5'), Decimal('50')),
    (Decimal('-2'), Decimal('3'), Decimal('-6')),
    (Decimal('0'), Decimal('5'), Decimal('0'))
])
def test_multiply(a, b, expected):
    """Test the multiply function in Calculator class."""
    assert Calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (Decimal('10'), Decimal('5'), Decimal('2')),
    (Decimal('-10'), Decimal('-2'), Decimal('5')),
    (Decimal('5'), Decimal('2'), Decimal('2.5'))
])
def test_divide(a, b, expected):
    """Test the divide function in Calculator class."""
    assert Calculator.divide(a, b) == expected

def test_divide_by_zero():
    """Ensure ValueError is raised for division by zero."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(Decimal('10'), Decimal('0'))
