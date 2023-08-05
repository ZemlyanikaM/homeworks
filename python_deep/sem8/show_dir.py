"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
    ○ Для дочерних объектов указывайте родительскую директорию.
    ○ Для каждого объекта укажите файл это или директория.
    ○ Для файлов сохраните его размер в байтах,
        а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
__all__ = ['show_dir']

import os
from pathlib import Path
import csv
import json
import pickle

F_NAME = 'Name'
F_PATH = 'Path'
F_SIZE = 'Size'
F_TYPE = 'Type'
F_PARENT = 'Parent'
F_DIRECTORY = 'Directory'
F_FILE = 'File'


def get_dir_size(path='.') -> int:
    size = 0
    with os.scandir(path) as current:
        for item in current:
            if item.is_file():
                size += item.stat().st_size
            elif item.is_dir():
                size += get_dir_size(item.path)
    return size


def get_size(path='.') -> int:
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_dir_size(path)


def show_dir(in_dir: Path):
    data = {}
    fieldnames = [F_NAME, F_PATH, F_SIZE, F_TYPE, F_PARENT]
    rows = []

    with (open('dirs.json', 'w') as f_json,
          open('dirs.csv', 'w', newline='', encoding='utf-8') as f_csv,
          open('dirs.pickle', 'wb') as f_pickle):

        for dir_path, dir_name, file_name in os.walk(in_dir):
            data.setdefault(dir_path, {})
            for d_path in dir_name:
                size = get_size(dir_path + '/' + d_path)
                data[dir_path].update({d_path: {F_SIZE: size, F_TYPE: F_DIRECTORY, F_PARENT: dir_path.split('/')[-1]}})
                rows.append({F_NAME: d_path, F_PATH: dir_path, F_SIZE: size, F_TYPE: F_DIRECTORY,
                             F_PARENT: dir_path.split('/')[-1]})
            for file in file_name:
                size = get_size(dir_path + '/' + file)
                data[dir_path].update(
                    {file: {F_SIZE: size, F_TYPE: F_FILE, F_PARENT: dir_path.split('/')[-1]}})
                rows.append({F_NAME: file, F_PATH: dir_path, F_SIZE: size, F_TYPE: F_FILE,
                             F_PARENT: dir_path.split('/')[-1]})

        json.dump(data, f_json, indent=2)
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        pickle.dump(f'{pickle.dumps(data)}', f_pickle)


if __name__ == '__main__':
    show_dir('.')
