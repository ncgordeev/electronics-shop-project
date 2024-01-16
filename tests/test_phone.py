import pytest
from src.phone import Phone


@pytest.fixture
def get_instance():
    return Phone("Iphone 15", 100, 20, 1)


def test_phone_init(get_instance):
    phone = get_instance
    assert phone.name == "Iphone 15"
    assert phone.number_of_sim == 1


def test_phone_repr(get_instance):
    phone = get_instance
    assert repr(phone) == "Phone('Iphone 15', 100, 20, 1)"


def test_number_of_sim(get_instance):
    phone = get_instance
    assert phone.number_of_sim == 1

    phone.number_of_sim = 3
    assert phone.number_of_sim == 3

    with pytest.raises(ValueError):
        phone.number_of_sim = 0
