# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
from pathlib import Path
from collections import namedtuple
import logging
import argparse

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)
File = namedtuple('File', 'name, extension, is_dir, parent_dir')


def parse_ars():
    parser = argparse.ArgumentParser(description="Directory reader")
    parser.add_argument('-p', '--path', default='.', help='Enter the directory path. ')
    args = parser.parse_args()
    return args.p


def read_dir(path: Path):
    for item in path.iterdir():
        f = File(item.stem if item.is_file() else item.name, item.suffix, item.is_dir(), item.parent)
        logger.info(f)
        if f.is_dir:
            read_dir(Path(f.parent_dir) / f.name)


if __name__ == '__main__':
    print(read_dir(Path('.')))
