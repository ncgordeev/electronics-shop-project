"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from config import ITEMS_CSV, ITEMS_CSV_ERR
from tests.fixture_item_instances import get_instance


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


@pytest.mark.parametrize(
    "value, expected",
    [
        ("5", 5),
        ("5.5", 5),
        ("5.0", 5),
    ]
)
def test_string_to_number(value, expected):
    new_val = Item.string_to_number(value)
    assert new_val == expected


def test_string_to_number_empty():
    with pytest.raises(ValueError, match="Значение не должно быть пустым!"):
        Item.string_to_number("")


def test_string_to_number_type_err():
    with pytest.raises(ValueError, match="Значение должно быть числом!"):
        Item.string_to_number("some")


def test_instantiate_from_csv():
    Item.instantiate_from_csv(ITEMS_CSV)
    assert len(Item.all) == 5


def test_instantiate_from_csv_err():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(ITEMS_CSV_ERR)


def test_instantiate_from_csv_item():
    Item.instantiate_from_csv(ITEMS_CSV)
    first_item = Item.all[0]
    assert first_item.name == "Смартфон"


def test_item_str(get_instance):
    instance_1, instance_2, instance_3 = get_instance
    assert str(instance_1) == "Смартфон"
    assert str(instance_2) == "НоутбукProSuper"
    assert str(instance_3) == ""


def test_item_repr(get_instance):
    instance_1, instance_2, instance_3 = get_instance
    assert repr(instance_1) == 'Item(Смартфон, 20, 10)'
    assert repr(instance_2) == 'Item(НоутбукProSuper, 200, 50)'
    assert repr(instance_3) == 'Item('', 0, 0)'


def test_item_add(get_instance):
    instance_1, instance_2, instance_3 = get_instance
    assert instance_1 + instance_2 == 60

    with pytest.raises(ValueError):
        instance_1 + 100
