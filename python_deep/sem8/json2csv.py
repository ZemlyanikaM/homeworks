"""
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
"""
__all__ = ['json2csv']

import csv
import json


def json2csv(json_src: str, csv_dst: str) -> None:
    with open(json_src, 'r', encoding='utf-8') as source_file:
        data = json.load(source_file)
    rows = []
    for access_level, users in data.items():
        for user_id, name in users.items():
            rows.append({'access_level': int(access_level),
                         'id': int(user_id),
                         'name': name})

    with open(csv_dst, 'w', encoding='utf-8') as dst_file:
        csv_dict = csv.DictWriter(dst_file, fieldnames=['access_level', 'id', 'name'], dialect='excel')
        csv_dict.writeheader()
        csv_dict.writerows(rows)


if __name__ == '__main__':
    json2csv('task2.json', 'task3.csv')
