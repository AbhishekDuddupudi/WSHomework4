import sys
import subprocess
import pytest

def run_cli(args):
    """Helper function to run main.py with provided arguments and capture output."""
    result = subprocess.run(
        [sys.executable, "main.py"] + args,
        capture_output=True,
        text=True,
        check=False  # Prevent subprocess.run from raising an exception on non-zero exit codes
    )
    return result.stdout.strip()

@pytest.mark.parametrize("args, expected", [
    (["5", "3", "add"], "The result of 5 add 3 is equal to 8.0"),
    (["10", "2", "subtract"], "The result of 10 subtract 2 is equal to 8.0"),
    (["4", "5", "multiply"], "The result of 4 multiply 5 is equal to 20.0"),
    (["20", "4", "divide"], "The result of 20 divide 4 is equal to 5.0"),
])
def test_valid_operations(args, expected):
    output = run_cli(args)
    assert expected in output

@pytest.mark.parametrize("args, expected", [
    (["1", "0", "divide"], "An error occurred: Cannot divide by zero"),
    (["9", "3", "unknown"], "Unknown operation: unknown"),
    (["a", "3", "add"], "Invalid number input: a or 3 is not a valid number.")
])
def test_error_conditions(args, expected):
    output = run_cli(args)
    assert expected in output
