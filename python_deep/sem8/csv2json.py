"""
# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка # csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.
"""
__all__ = ['csv2json']

import csv
import json


def csv2json(csv_src: str, json_dst: str) -> None:
    with open(csv_src, 'r', encoding='utf-8') as cf:
        data_in = csv.reader(cf, dialect='excel')
        data = []
        for i, line in enumerate(data_in):
            if i:
                access_level, user_id, name = line
                user_data = {}
                user_data['access_level'] = int(access_level)
                user_data['user_id'] = f'{int(user_id):010}'
                user_data['name'] = name.capitalize()
                user_data['hash'] = hash((user_id, name))
                data.append(user_data)

    with open(json_dst, 'w', encoding='utf-8') as jf:
        json.dump(data, jf, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    csv2json('task3.csv', 'task4.json')
