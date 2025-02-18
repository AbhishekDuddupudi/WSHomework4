"""
This module contains tests for the Calculations class.
It verifies that the calculation history functionality works correctly.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

# Create a fixture that will be used only for its side effects.
@pytest.fixture(name="_calc_history")
def calc_history_fixture():
    """Fixture to clear history and add sample calculations."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(_calc_history):
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add calculation."

def test_get_history(_calc_history):
    """Test retrieving the calculation history."""
    history = Calculations.get_history()
    assert len(history) == 2, "History count mismatch."

def test_clear_history(_calc_history):
    """Test clearing the calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared."

def test_get_latest(_calc_history):
    """Test retrieving the latest calculation."""
    latest = Calculations.get_latest()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Latest calculation incorrect."

def test_find_by_operation(_calc_history):
    """Test finding calculations by operation."""
    add_ops = Calculations.find_by_operation("add")
    assert len(add_ops) == 1, "Add operations count mismatch."
    subtract_ops = Calculations.find_by_operation("subtract")
    assert len(subtract_ops) == 1, "Subtract operations count mismatch."

def test_get_latest_with_empty_history():
    """Test get_latest returns None when history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None with empty history."
