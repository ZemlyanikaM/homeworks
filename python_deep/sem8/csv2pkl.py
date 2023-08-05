"""# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку
"""
__all__ = ['csv2pkl']

import pickle
import csv


def csv2pkl(csv_dst: str) -> None:
    with open(csv_dst, 'r', encoding='utf-8') as csvf:
        csv_reader = csv.reader(csvf, dialect='excel')
        data_list = []
        headers = []
        for i, row in enumerate(csv_reader):
            if not i:
                headers = row
            else:
                row_data = {key: value for key, value in zip(headers, row)}
                data_list.append(row_data)

    print(pickle.dumps(data_list))


if __name__ == '__main__':
    csv2pkl('task6.csv')
