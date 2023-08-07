"""
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
"""

__all__ = ['coef_gen2csv']

import csv
from random import randint as rnd

MIN_ROWS = 3
MAX_ROWS = 10


def coef_gen2csv():
    with open('coefficients.csv', 'w', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        for row in range(rnd(MIN_ROWS, MAX_ROWS + 1)):
            writer.writerow([rnd(-1000, 1000), rnd(-1000, 1000), rnd(-1000, 1000)])
