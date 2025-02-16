import sys
import subprocess

def run_cli(args):
    """Helper to run main.py with provided arguments and capture output."""
    result = subprocess.run(
        [sys.executable, "main.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def test_cli_add():
    output = run_cli(["5", "3", "add"])
    expected = "The result of 5 add 3 is equal to 8.0"
    assert expected in output

def test_cli_subtract():
    output = run_cli(["10", "2", "subtract"])
    expected = "The result of 10 subtract 2 is equal to 8.0"
    assert expected in output

def test_cli_multiply():
    output = run_cli(["4", "5", "multiply"])
    expected = "The result of 4 multiply 5 is equal to 20.0"
    assert expected in output

def test_cli_divide():
    output = run_cli(["20", "4", "divide"])
    expected = "The result of 20 divide 4 is equal to 5.0"
    assert expected in output

def test_divide_by_zero():
    output = run_cli(["1", "0", "divide"])
    expected = "An error occurred: Cannot divide by zero"
    assert expected in output

def test_unknown_operation():
    output = run_cli(["9", "3", "unknown"])
    expected = "Unknown operation: unknown"
    assert expected in output

def test_invalid_input():
    output = run_cli(["a", "3", "add"])
    expected = "Invalid number input: a or 3 is not a valid number."
    assert expected in output
