"""
# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
"""
__all__ = ['json2pkl']

import json
import os
import pickle


def json2pkl(dir_path: str) -> None:
    json_files = filter(lambda file_name: file_name[-5:] == '.json', os.listdir(dir_path))
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as jf:
            data = json.load(jf)
        with open(f'{json_file[:-5]}.pickle', 'wb') as pf:
            pickle.dump(data, pf)


if __name__ == '__main__':
    json2pkl('.')
