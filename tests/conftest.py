import pytest
from faker import Faker

def pytest_addoption(parser):
    parser.addoption(
        "--num_records",
        action="store",
        default=10,
        type=int,
        help="Number of test records to generate"
    )

@pytest.fixture
def fake():
    return Faker()

def calculate_expected(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        # In a real scenario, you might want to ensure b is not zero.
        return a / b if b != 0 else "Error: Division by zero"
    else:
        raise ValueError(f"Unknown operation: {operation}")

@pytest.fixture
def generated_data(request, fake):
    num_records = request.config.getoption("--num_records")
    data = []
    for _ in range(num_records):
        a = fake.random_int(min=1, max=100)
        b = fake.random_int(min=1, max=100)
        operation = fake.random_element(elements=("add", "subtract", "multiply", "divide"))
        expected = calculate_expected(a, b, operation)
        data.append((a, b, operation, expected))
    return data
