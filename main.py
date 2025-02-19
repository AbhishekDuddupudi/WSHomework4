import sys
from calculator import Calculator 

def print_usage_and_exit():
    print("Usage: python main.py <a> <b> <operation>")
    sys.exit(1)

def main():
    # Validate that exactly 3 arguments are provided.
    if len(sys.argv) != 4:
        print_usage_and_exit()

    a_str, b_str, operation = sys.argv[1:4]

    # Convert the input strings to floats.
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print(f"Invalid number input: {a_str} or {b_str} is not a valid number.")
        sys.exit(1)

    # Create an instance of Calculator.
    calc = Calculator()

    # Map operations to the corresponding Calculator methods.
    operations = {
        "add": calc.add,
        "subtract": calc.subtract,
        "multiply": calc.multiply,
        "divide": calc.divide,
    }

    if operation not in operations:
        print(f"Unknown operation: {operation}")
        sys.exit(1)

    try:
        result = operations[operation](a, b)
        print(f"The result of {a_str} {operation} {b_str} is equal to {result}")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
