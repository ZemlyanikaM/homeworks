"""Deco for guess the number game"""
__all__ = ['param_deco']

from functools import wraps
from typing import Callable


def param_deco(calls_qty: int) -> Callable:
    results = []

    def deco(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(calls_qty):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return deco


@param_deco(5)
def sum_nums(*agrs):
    return sum(agrs)


if __name__ == '__main__':
    print(sum_nums(1, 2, 3, 4))
