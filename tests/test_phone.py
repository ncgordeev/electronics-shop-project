import pytest
from src.phone import Phone


@pytest.fixture
def get_instance():
    return Phone("Iphone 15", 100, 20, 1)


def test_phone_init(get_instance):
    phone = get_instance
    assert phone.name == "Iphone 15"
    assert phone.sim_quantity == 1
