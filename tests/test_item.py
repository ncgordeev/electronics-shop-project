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


@pytest.mark.parametrize(
    "instance, pay_ratio, expected",
    [
        (Item("Смартфон", 20, 10), 0.5, 10.0),
        (Item("Ноутбук", 200, 50), 0.1, 20.0),
        (Item("Пылесос", 100, 0), 0.9, 90),
    ]
)
def test_apply_discount(instance, pay_ratio, expected):
    instance.pay_rate = pay_ratio
    instance.apply_discount()
    assert instance.price == expected


@pytest.mark.parametrize(
    "instance, expected",
    [
        (Item("Смартфон", 20, 10), "Смартфон"),
        (Item("НоутбукProSuper", 200, 50), "НоутбукProSuper"),
        (Item("", 0, 0), ""),
    ]
)
def test_name_getter(instance, expected):
    good_name = instance.name
    assert good_name == expected


def test_name_setter():
    item = Item("НоутбукProSuper", 200, 50)
    item.name = "Ноутбук"
    assert item.name == "Ноутбук"


def test_name_setter_too_long():
    item = Item("НоутбукProSuper", 200, 50)
    item.name = "НоутбукProSuper"
    assert item.name == "НоутбукPro"


def test_name_setter_empty_value():
    item = Item("", 200, 50)
    with pytest.raises(ValueError, match="Наименование не должно быть пустым"):
        item.name = ""
