"""
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
"""
__all__ = ['create_json']

import json


def create_json(path: str = './result.txt', path_json: str = './result.json') -> None:
    in_dict = {}
    with open(path, 'r', encoding='utf-8') as src:
        for line in src:
            name, num = line.split('|')
            in_dict[name.capitalize()] = float(num)

    with open(path_json, 'w', encoding='utf-8') as dst:
        json.dump(in_dict, dst, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    create_json()
