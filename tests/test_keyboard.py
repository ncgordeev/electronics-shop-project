import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def kb_instance():
    return Keyboard("Dark Project KD87A", 9600, 5)


def test_keyboard_init(kb_instance):
    kb = kb_instance
    assert kb.name == "Dark Project KD87A"
    assert kb.language == "EN"


def test_keyboard_repr(kb_instance):
    kb = kb_instance
    assert repr(kb) == "Keyboard('Dark Project KD87A', 9600, 5, EN)"


def test_keyboard_change_lang(kb_instance):
    kb = kb_instance
    assert kb.language == "EN"

    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"
