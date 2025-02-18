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

# Use a fixture name that can be shared among tests.
@pytest.fixture(name="faker_instance")
def fixture_faker_instance():
    return Faker()

def calculate_expected(a, b, operation):
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        return a / b if b != 0 else "Error: Division by zero"
    raise ValueError(f"Unknown operation: {operation}")

@pytest.fixture
def generated_data(request, faker_instance):
    num_records = request.config.getoption("--num_records")
    data = []
    for _ in range(num_records):
        a = faker_instance.random_int(min=1, max=100)
        b = faker_instance.random_int(min=1, max=100)
        # Break this line into multiple lines to avoid exceeding the line limit.
        operation = faker_instance.random_element(
            elements=("add", "subtract", "multiply", "divide")
        )
        expected = calculate_expected(a, b, operation)
        data.append((a, b, operation, expected))
    return data
