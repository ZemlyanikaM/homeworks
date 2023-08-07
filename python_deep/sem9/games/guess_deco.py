"""deco for guess the number game"""

__all__ = ['deco']

import random
from typing import Callable
from functools import wraps


def deco(func: Callable) -> Callable[[int, int], None]:
    min_num = 1
    max_num = 100
    min_atmpt = 1
    max_atmpt = 10

    @wraps(func)
    def wrapper(num: int, attempts: int, *args, **kwargs):
        if not min_num <= num <= max_num:
            num = random.randint(min_num, max_num + 1)
        if not min_atmpt <= attempts <= max_atmpt:
            attempts = random.randint(min_atmpt, max_atmpt + 1)
        return func(num, attempts, *args, **kwargs)

    return wrapper

#
# @deco
# def puzzle(num: int, attempts: int):
#     for i in range(1, attempts + 1):
#         print(f'Attempt: {i}')
#         user_answer = int(input("Enter a number: "))
#         if user_answer == num:
#             print('You won!')
#             return
#         elif user_answer > num:
#             print(f'The {user_answer} is bigger.')
#         else:
#             print(f'The {user_answer} is smaller.')
#
#
# if __name__ == '__main__':
#     puzzle(1546, 14)
