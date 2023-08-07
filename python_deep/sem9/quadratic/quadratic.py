"""
Нахождение корней квадратного уравнения
"""
__all__ = ['quadratic']

import math
from log2json import log2json
from load_csv import load_csv


@load_csv
@log2json
def quadratic(*args) -> tuple | float | None:
    a, b, c = args
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif d == 0:
        x = -b / (2 * a)
        return round(x, 2)
