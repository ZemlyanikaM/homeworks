"""# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""
__all__ = ['pkl2csv']

import pickle
import csv


def pkl2csv(pkl_src: str, csv_dst: str) -> None:
    with open(pkl_src, 'rb') as pf:
        data_in = pickle.load(pf)
    headers = data_in[0].keys()

    with open(csv_dst, 'w', encoding='utf-8') as csvf:
        csw_writer = csv.DictWriter(csvf, fieldnames=headers, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csw_writer.writeheader()
        csw_writer.writerows(data_in)


if __name__ == '__main__':
    pkl2csv('task4.pickle', 'task6.csv')
