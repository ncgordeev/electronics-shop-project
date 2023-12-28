"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.mark.parametrize(
    "instance, expected",
    [
        (Item("Смартфон", 20, 10), 200),
        (Item("Ноутбук", 200, 50), 10000),
        (Item("Пылесос", 10, 0), 0),
    ]
)
def test_calculate_total_price(instance, expected):
    total_price = instance.calculate_total_price()
    assert total_price == expected
