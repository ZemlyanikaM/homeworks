"""Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла."""
__all__ = ['load_csv']

import csv
from typing import Callable
from coef_gen2csv import coef_gen2csv as coef


def load_csv(function: Callable):
    coef()

    def wrapper():
        with open('coefficients.csv', 'r', encoding='UTF-8') as csv_file:
            data = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
            for values in data:
                if values and values[0] != 0:
                    function(*values)

    return wrapper
