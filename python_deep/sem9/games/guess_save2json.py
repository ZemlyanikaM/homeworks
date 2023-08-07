"""logger for guess the number game"""
__all__ = ['save2json']

from functools import wraps
from typing import Callable
import json
from os.path import exists


def save2json(func: Callable) -> Callable[[list, dict], int]:

    @wraps(func)
    def wrapper(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        data_list = []
        if exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as json_file:
                data_list = json.load(json_file)
        result = func(*args, **kwargs)
        current_data = {
            'args': args,
            **kwargs,
            'result': result
        }
        data_list.append(current_data)
        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=2, ensure_ascii=False)
        return result

    return wrapper

#
# @save2json
# def sum_nums(*args, **kwargs) -> int:
#     return sum(args)
#
#
# @save2json
# def str_conc(*args, **kwargs) -> str:
#     return ''.join(args)
#
#
# if __name__ == '__main__':
#     sum_nums(421, 615, 41, x=1, y=2, z=3)
#     str_conc('Hello', 'my', 'dear', 'friend')
