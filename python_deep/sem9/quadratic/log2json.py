"""
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""
__all__ = ['log2json']

import datetime
import json
import os
from typing import Callable


def log2json(func: Callable):
    """
    logger to log.json for quadratic
    """
    result = {}
    if os.path.exists('log.json'):
        with open('log.json', 'r', encoding='UTF-8') as json_file:
            result = json.load(json_file)
    else:
        with open('log.json', 'w', encoding='UTF-8') as json_file:
            json.dump(result, json_file)

    def wrapper(*args):
        solutions = func(*args)
        sol_dict = {'a': args[0], 'b': args[1], 'c': args[2], 'roots': solutions}
        res_key = f'{datetime.datetime.now()}'[:-7]
        result[res_key] = result.get(res_key) + [sol_dict] if result.get(res_key) else [sol_dict]
        with open('log.json', 'w', encoding='UTF-8', ) as json_file:
            json.dump(result, json_file, indent=4, ensure_ascii=False)
        return solutions

    print("Solution added to log.json")
    return wrapper
