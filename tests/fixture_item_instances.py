import pytest
from src.item import Item


@pytest.fixture
def get_instance():
    return [
        Item("Смартфон", 20, 10),
        Item("НоутбукProSuper", 200, 50),
        Item("", 0, 0),
    ]
