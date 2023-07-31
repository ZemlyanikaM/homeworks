"""
Directory creator
"""
__all__ = ['mkd']

import os
from os import path


def mkd(dir: str) -> None:
    if not path.exists(dir):
        os.mkdir(dir)
