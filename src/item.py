from csv import DictReader
from exceptions import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if 0 < len(name) < 10:
            self.__name = name
        elif len(name) == 0:
            raise ValueError("Наименование не должно быть пустым")
        else:
            self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path):
        """
        This method initialize the class instances from file
        """
        try:
            with open(file_path, encoding="windows-1251") as file:
                cls.all.clear()
                reader = DictReader(file)
                for row in reader:
                    cls(
                        name=row["name"],
                        price=float(row["price"]),
                        quantity=cls.string_to_number(row["quantity"]),
                    )
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file_path} не найден. Проверьте путь.")

        except KeyError:
            raise InstantiateCSVError(f"Файл {file_path} поврежден")

    @staticmethod
    def string_to_number(string_to_num):
        """
        This method convert string-number to number
        """
        if len(string_to_num) == 0:
            raise ValueError("Значение не должно быть пустым!")
        elif string_to_num.isalpha():
            raise ValueError("Значение должно быть числом!")
        else:
            numbers = string_to_num.split(".")
            number = int(numbers[0])
            return number

    def __str__(self) -> str:
        return f"{self.__name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__name}, {self.price}, {self.quantity})"

    def __add__(self, other):
        """
        This method allows additions instances of a class with each other
        """

        if isinstance(other, self.__class__) or issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        else:
            raise AttributeError("Складывать можно только экземпляры класса Item и дочерние от него")
