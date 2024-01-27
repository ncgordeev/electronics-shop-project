from src.item import Item
from config import ITEMS_CSV_ERR, ITEMS_CSV_CORRUPTED

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    # Item.instantiate_from_csv(ITEMS_CSV_ERR)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(ITEMS_CSV_CORRUPTED)
    # InstantiateCSVError: Файл item.csv поврежден
