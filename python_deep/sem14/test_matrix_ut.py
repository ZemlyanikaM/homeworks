import unittest
from matrix import Matrix


class TestMatrix(unittest.TestCase):

    def test_add(self):
        self.assertEqual(str(Matrix([[1, 2], [3, 4]]) + Matrix([[5, 6], [7, 8]])), '[6, 8][10, 12]')

    def test_mul(self):
        self.assertEqual(str(Matrix([[1, 2], [3, 4]]) * Matrix([[5, 6], [7, 8]])), '[19, 22][43, 50]')

    def test_eq(self):
        self.assertTrue(Matrix([[1, 2], [3, 4]]) == Matrix([[1, 2], [3, 4]]))


if __name__ == '__main__':
    unittest.main(verbosity=2)
