import pytest
from matrix import Matrix


def test_matrix_add():
    assert (str(Matrix([[1, 2], [3, 4]]) + Matrix([[5, 6], [7, 8]]))) == '[6, 8][10, 12]'


def test_matrix_mul():
    assert (str(Matrix([[1, 2], [3, 4]]) * Matrix([[5, 6], [7, 8]]))) == '[19, 22][43, 50]'


if __name__ == '__main__':
    pytest.main(['vv'])
