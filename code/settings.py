# Путь до файла
FILENAME = "./sochi_kom.xlsx"

# Имя товара
TOVAR_NAME = 'sochi_com'

# Количество дней в месяце
COUNT_DAYS_OF_MONTH = 30
# Первый день в колонках
FIRST_DAY_COLUMN = 3
# Количество строчек
COUNT_ROWS = 107
# Первая строчка
FIRST_ROW = 2

NAMES = ['Фил', 'Джек', 'Рокс', 'Остин', 'Коллинс', 'Гуливер']
REPLACE_NAMES = {
    'FFFFFF00': 'Фил',
    'FFC4BD97': 'Джек',
    'FF7030A0': 'Рокс',
    'FF00B0F0': 'Остин',
    'FFFFC000': 'Коллинс',
    'FF92D050': 'Гуливер'
}
FULL_TEXT = 'Комод ""'


# В течении скольких часов, будут идти публикации
START_HOUR_POSTING = 2 # С какого часа дня начинаем публикации
DELTA_FOR_POSTING = 22 # Сколько часов с моммента START_HOUR_POSTING идут обьявления

TIMES_BY_COLORS = {
    '00000000': 9,
}
