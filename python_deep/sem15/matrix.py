import logging

logging.basicConfig(filename='log.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} function "{funcName}()" line {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class Matrix:
    def __init__(self, matrix):
        self._matrix = matrix

    def __check_sizes(self, other):
        return len(self._matrix) != len(other._matrix) or len(self._matrix[0]) != len(other._matrix[0])

    def get_matrix(self):
        return self._matrix

    def __add__(self, other):
        if self.__check_sizes(other):
            logger.error(f'Addition  is not possible! The wrong size of the matrices: \
            [{len(self._matrix)}][{len(self._matrix[0])}] !=  [{len(other._matrix)}][{len(other._matrix[0])}]')
            # raise SizesException('add')
        else:
            result = Matrix([[self._matrix[i][j] + other._matrix[i][j] for j in range(len(self._matrix[0]))] \
                             for i in range(len(self._matrix))])
            logger.info(f'Addition: {self._matrix} + {other._matrix} = {result}')
            return result

    def __mul__(self, other):
        if len(self._matrix[0]) != len(other._matrix):
            logger.error(f'Multiplication  is not possible! The wrong size of the matrices: ')
            # raise SizesException('mul')
        else:
            mul_matrix = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matrix)] \
                          for i_row in self._matrix]
            logger.info(f'Multiplication: {self._matrix} * {other._matrix} = {mul_matrix}')
            return Matrix(mul_matrix)

    def __eq__(self, other):
        if self.__check_sizes(other):
            logger.error(f'Comparison is not possible! The wrong size of the matrices')
            # raise SizesException('eq')
        else:
            for i in range(len(self._matrix)):
                for j in range(len(self._matrix[0])):
                    if self._matrix[i][j] != other._matrix[i][j]:
                        logger.info(f'{self._matrix} != {other._matrix}')
                        return False
            logger.info(f'{self._matrix} = {other._matrix}')
            return True

    # def __str__(self):
    #     s = ''
    #     for i in range(len(self._matrix)):
    #         s += str(self._matrix[i]) + '\n'
    #     return s

    def __repr__(self):
        s = ''
        for i in range(len(self._matrix)):
            s += str(self._matrix[i])
        return s


if __name__ == '__main__':
    m_1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           [10, 11, 12]]

    m_2 = [[12, 11, 10],
           [9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

    m_3 = [[0, 1, 2, 3],
           [4, 5, 6, 7],
           [8, 9, 10, 11]]

    m_4 = [[12, 13, 14, 15, 16],
           [17, 18, 19, 20, 21],
           [22, 23, 24, 25, 26]]

    matrix_1 = Matrix(m_1)
    matrix_2 = Matrix(m_2)
    matrix_3 = Matrix(m_3)
    matrix_4 = Matrix(m_4)

    print("__add__")
    print(matrix_1 + matrix_2)
    print(matrix_1 + matrix_3)
    print()
    print("__mul__")
    print(matrix_1 * matrix_4)
    print(matrix_1 * matrix_2)
    print()
    print("__eq__")
    print(matrix_1 == matrix_1)
    print(matrix_1 == matrix_2)
    print(matrix_1 == matrix_3)
