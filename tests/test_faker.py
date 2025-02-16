import pytest
from faker import Faker

# Create a pytest fixture for the Faker instance
@pytest.fixture
def fake():
    return Faker()

def test_fake_name(fake):
    name = fake.name()
    assert isinstance(name, str) and name.strip() != "", "Generated name should be a non-empty string"

def test_fake_address(fake):
    address = fake.address()
    assert isinstance(address, str) and address.strip() != "", "Generated address should be a non-empty string"

def test_fake_text(fake):
    text = fake.text(max_nb_chars=50)
    assert isinstance(text, str) and text.strip() != "", "Generated text should be a non-empty string"
