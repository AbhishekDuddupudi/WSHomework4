# Intermediate Calculator (Part 2)

This is an intermediate-level Python calculator that uses object-oriented programming principles. It performs basic arithmetic operations and utilizes a `Calculator` class with static methods and a `Calculation` class to store operations.

## Features
- Addition, subtraction, multiplication, and division
- Uses a `Calculator` class with static methods for operations
- Uses a `Calculation` class to store values and perform operations
- Error handling for division by zero

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/AbhishekDuddupudi/WShomework3.git
   cd calculator_project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests
To run tests, use:
```bash
pytest tests/
```

## Usage
You can use the calculator functions in Python:
```python
from calculator import Calculator

result = Calculator.add(10, 5)
print(result)  # Output: 15
```

This project demonstrates object-oriented principles such as encapsulation and separation of concerns.

