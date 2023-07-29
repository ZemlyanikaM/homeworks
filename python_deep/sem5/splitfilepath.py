import os

path = os.path.abspath('splitpath.py')
print(path)


def splitpath(path: str) -> tuple:
    path, fname = os.path.split(path)
    name, ext = fname.split('.')
    return path, name, ext


print(splitpath(path))
