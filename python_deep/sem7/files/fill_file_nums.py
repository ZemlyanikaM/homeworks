"""
# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.
"""
__all__ = ['fill_file_nums']

from random import randint, uniform

START = -1000
END = 1001


def fill_file_nums(file_name: str = "data.txt", lines: int = 3):
    with open(file_name, mode='w', encoding='utf-8') as file:
        for _ in range(lines):
            int_num = randint(START, END)
            float_num = uniform(START, END)
            file.write(f'{int_num}|{float_num}\n')


fill_file_nums()
