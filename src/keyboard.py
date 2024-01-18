from src.item import Item


class Mixin:
    __language = "EN"

    def __init__(self):
        self.__language = self.__language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        This method switch current language
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(Item, Mixin):

    def __init__(self, name: str, price: float, quantity: int, ) -> None:
        super().__init__(name, price, quantity)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.language})"
