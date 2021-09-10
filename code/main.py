from openpyexcel import load_workbook
from models import Post
from settings import *
from work import Solver
from math import ceil
from datetime import date, timedelta
import datetime

def key_function(post):
    return (post.rr, cites.index(post.city), post.get_time())


def write_posts_in_send(posts):
    global wbv
    sheet = wb["send"]
    index = 3
    cities = dict()
    for post in posts:
        if post.city not in cities:
            cities[post.city] = 1001
        cell = sheet.cell(column=2, row=index)
        sheet[cell.coordinate] = post.get_time()
        cell = sheet.cell(column=7, row=index)
        sheet[cell.coordinate] = post.city
        cell = sheet.cell(column=1, row=index)
        sheet[cell.coordinate] = f'{TOVAR_NAME}_{post.socr}_{cities[post.city]}'
        cell = sheet.cell(column=19, row=index)
        sheet[cell.coordinate] = post.description
        index += 1
        cities[post.city] += 1
    wb.save(FILENAME)


wb = load_workbook(FILENAME)


sheet = wb["posts"]
wb.save(filename=FILENAME)


posts = []

first_day = FIRST_DAY_COLUMN + 1
last_day = first_day + COUNT_DAYS_OF_MONTH
start_row = FIRST_ROW
end_row = start_row + COUNT_ROWS


print('Цвет     - позиция в таблице')

all_colors = []
cites = []
current_day = 1
flag = 1

for column in range(first_day, last_day + 1):
    for row in range(start_row, end_row):
        city_name = sheet.cell(row=row, column=1).value
        cites.append(city_name)
        if city_name:
            current_city_name = city_name
        furniture_type = 'диван' # sheet.cell(row=row, column=2).value

        date = sheet.cell(row=1, column=column).value

        cell = sheet.cell(row=row, column=column)
        value = cell.value
        color = cell.fill.start_color.index
        socr = sheet.cell(row=row, column=2).value
        if color in REPLACE_NAMES:
            replace_text = REPLACE_NAMES[color]
        else:
            replace_text = 'lala'

        if color not in all_colors:
            print(color, '-', cell.coordinate)
            all_colors.append(color)

        if type(value) == int:
            for i in range(value):
                post = Post(row, value, current_city_name, color, column, furniture_type)
                post.socr = socr
                post.description = FULL_TEXT.replace('{{}}', replace_text)
                post.rr = NAMES.index(replace_text)
                if flag:
                    date0 = date
                    #date1= date.today()
                    date_str = input("Введите дату в формате dd.mm.yyyy или любой символ если дату не нужно смещать: ")
                    date_list = date_str.split('.')
                    if len(date_list) < 3:
                        date1 = date0
                    else:
                        date1 = datetime.datetime(int(date_list[2]), int(date_list[1]), int(date_list[0]))
                    date_delta = date1 - date0

                    flag = 0
                #print(date, date + date_delta)
                date_new = date + date_delta
                post.time.day = date_new.day
                post.time.month = date_new.month
                post.time.year = date_new.year
                posts.append(post)
    current_day += 1
print(all_colors)

""""
print('Начало обнуления, прошлых значений')
for post in posts:
    cell = sheet.cell(
            column=post.column+COUNT_DAYS_OF_MONTH+2,
            row=post.row
    )
    sheet[cell.coordinate] = ''
wb.save(FILENAME)
print('Обнуление завершенно')
"""

print('Начало бизнес-логики')
posts = Solver(posts).run()
"""
for key, value in data.items():
    for post in value:
        if not post.has_time():
            continue
        cell = sheet.cell(
            column=post.column+COUNT_DAYS_OF_MONTH + 2,
            row=post.row
        )
        for_write = post.get_time()
        print(for_write)
        if cell.value:
            for_write = cell.value + ", " + for_write
        sheet[cell.coordinate] = for_write

wb.save(filename=FILENAME)
"""
posts.sort(key=key_function)
write_posts_in_send(posts)
print('Конец бизнес-логики')
print('Завершение работы')
