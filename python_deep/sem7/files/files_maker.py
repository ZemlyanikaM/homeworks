"""
file maker
"""
__all__ = ['files_gen']

import os
from string import ascii_lowercase, digits
from random import choices, randint


def make_files(ext: str, max_name: int = 8, min_name: int = 4,
               min_size: int = 256, max_size: int = 4096, quantity: int = 5) -> None:
    for _ in range(quantity):
        name = ''.join(choices(ascii_lowercase + digits + "_", k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(rf'{name}.{ext}', 'wb') as file:
            file.write(data)


def files_gen(directory: str, sample: dict):
    os.chdir(directory)
    for ext, quantity in sample.items():
        make_files(ext, quantity=quantity)
