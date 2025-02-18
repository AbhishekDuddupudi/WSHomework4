def test_fake_name(faker_instance):
    name = faker_instance.name()
    assert isinstance(name, str) and name.strip() != "", "Empty name"

def test_fake_address(faker_instance):
    address = faker_instance.address()
    assert isinstance(address, str) and address.strip() != "", "Empty address"

def test_fake_text(faker_instance):
    text = faker_instance.text(max_nb_chars=50)
    assert isinstance(text, str) and text.strip() != "", "Empty text"
