"""
files sorter
"""
__all__ = ['sort_files']

import os
from pathlib import Path
import shutil
from .mkd import mkd


def sort_files(src: str, dst: str):
    os.chdir("..")
    mkd(dst)

    src_path = Path(Path.cwd() / src)
    dst_path = Path(Path.cwd() / dst)

    files = os.listdir(src_path)

    for items in files:
        ext = items.split('.')

        if len(ext) > 1 and (
                ext[1].lower() == "png" or
                ext[1].lower() == "jpg" or
                ext[1].lower() == "img"):
            file = str(src_path) + '/' + items
            new_path = str(dst_path) + "/Pic/" + items
            print(new_path)
            mkd(str(dst_path) + "/Pic/")
            shutil.move(file, new_path)
        elif len(ext) > 1 and (ext[1].lower() == 'mp4' or
                               ext[1].lower() == 'mpg' or
                               ext[1].lower() == 'avi'):
            file = str(src_path) + "/" + items
            new_path = str(dst_path) + "/Video/" + items
            mkd(str(dst_path) + "/Video/")
            shutil.move(file, new_path)
        elif len(ext) > 1 and (ext[1].lower() == 'txt' or
                               ext[1].lower() == 'md' or
                               ext[1].lower() == 'pdf'):
            file = str(src_path) + "/" + items
            new_path = str(dst_path) + "/Doc/" + items
            mkd(str(dst_path) + "/Doc/")
            shutil.move(file, new_path)
        elif len(ext) > 1 and (ext[1].lower() == 'tar' or
                               ext[1].lower() == 'gz' or
                               ext[1].lower() == 'zip'):
            file = str(src_path) + "/" + items
            new_path = str(dst_path) + "/Arch/" + items
            mkd(str(dst_path) + "/Arch/")
            shutil.move(file, new_path)
