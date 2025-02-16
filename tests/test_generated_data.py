def test_generated_data_length(generated_data, request):
    # Get the expected number of records from the pytest config
    num_records = request.config.getoption("--num_records")
    assert len(generated_data) == num_records


def test_generated_data_content(generated_data):
    # Test that each record has four elements: a, b, operation, and expected result.
    for record in generated_data:
        assert len(record) == 4
