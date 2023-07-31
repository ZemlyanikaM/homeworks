"""
files renamer
"""
__all__ = ['mvf']

import os
from pathlib import Path


def mvf(ext_src: str, ext_dst: str, range_: list[int], digits: int, added_name: str = ''):
    num = 0
    for file in os.listdir():
        if file.endswith(ext_src):
            num += 1
            Path(file).rename(f"{file.split('.')[0][range_[0]:range_[1]]}{added_name}{num:0>{digits}}.{ext_dst}")
