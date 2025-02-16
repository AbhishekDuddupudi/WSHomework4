import sys
from calculator import Calculator  

def main():
    # Expecting exactly 3 arguments: a, b, and operation.
    if len(sys.argv) != 4:
        print("Usage: python main.py <a> <b> <operation>")
        sys.exit(1)

    a_str, b_str, operation = sys.argv[1:4]

    # Validate numeric inputs.
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print(f"Invalid number input: {a_str} or {b_str} is not a valid number.")
        sys.exit(1)

    calc = Calculator()  

    try:
        if operation == "add":
            result = calc.add(a, b)
        elif operation == "subtract":
            result = calc.subtract(a, b)
        elif operation == "multiply":
            result = calc.multiply(a, b)
        elif operation == "divide":
            result = calc.divide(a, b)
        else:
            print(f"Unknown operation: {operation}")
            sys.exit(1)

        print(f"The result of {a_str} {operation} {b_str} is equal to {result}")

    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
