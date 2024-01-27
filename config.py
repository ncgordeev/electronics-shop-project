import os

ROOT_PATH = os.path.dirname(__file__)
ITEMS_CSV = os.path.join(ROOT_PATH, "src", "items.csv")
ITEMS_CSV_ERR = os.path.join(ROOT_PATH, "src", "items_err.csv")
ITEMS_CSV_CORRUPTED = os.path.join(ROOT_PATH, "tests", "test_items_corrupted.csv")
