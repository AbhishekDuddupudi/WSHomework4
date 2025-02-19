# Advanced Calculator

This repository showcases the evolution of a Python-based calculator from basic operations to advanced features like dynamic testing with Faker and a command-line interface (CLI).

## Features

1. **Arithmetic Operations**  
   - Supports addition, subtraction, multiplication, and division.
   - Organized using OOP principles with classes such as `Calculation`, `Calculations`, and `Calculator`.

2. **Faker Integration**  
   - Uses the Faker library to generate synthetic data for testing.
   - Allows dynamic test data generation via a custom pytest command-line option (e.g., `--num_records`).

3. **Command-Line Interface (CLI)**  
   - Implements a `main.py` file to handle user inputs.
   - Validates numeric inputs, handles division by zero, and recognizes unknown operations.
   - Provides user-friendly error messages.

4. **Comprehensive Testing**  
   - Unit tests covering core arithmetic operations, Faker usage, and CLI behavior.
   - Pytest fixtures and parameterized tests for flexible, robust test coverage.
   - Easily executed with `pytest`.

## Installation & Setup

1. **Clone the Repository**  
   ```bash
   git clone <your-repo-link.git>
   cd <repo-name>

2. **Create & Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   (On Windows: venv\Scripts\activate)

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Tests**
   ```bash
   pytest --num_records=20


![alt text](<../../Screenshot 2025-02-18 at 7.55.01 PM.png>)

![alt text](<../../Screenshot 2025-02-18 at 7.55.44 PM.png>)