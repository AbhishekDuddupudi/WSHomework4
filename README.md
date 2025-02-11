# Advanced Calculator (Part 3)

This is an advanced Python calculator that follows Object-Oriented Programming (OOP) principles, implementing SOLID design patterns. It supports arithmetic operations, calculation history, and enhanced testing with parameterized test data and fixtures.

## Features
- Perform basic arithmetic operations: addition, subtraction, multiplication, and division.
- Uses a `Calculator` class with static methods to perform calculations.
- Uses a `Calculation` class to store values and execute operations.
- Implements a `Calculations` class to maintain a history of performed calculations.
- Exception handling for division by zero.
- Uses `pytest` for unit testing with parameterized test cases and fixtures.
- Follows best practices in software design (Single Responsibility Principle, Encapsulation, DRY).

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
To run tests and check test coverage, use:
```bash
pytest tests/ --cov=calculator
```
