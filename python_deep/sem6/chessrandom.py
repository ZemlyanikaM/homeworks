"""
random board
"""
__all__ = ['find_solutions']

from chess import check_the_board
from random import randint as rnd


def find_solutions(arrangements):
    board = 8
    solution = []
    count = 1
    while count <= arrangements:
        i = 0
        while i < board:
            x = rnd(1, 8)
            y = rnd(1, 8)
            if [x, y] not in solution:
                solution.append([x, y])
                i += 1
        if check_the_board(solution):
            print(solution)
            count += 1
        solution.clear()


if __name__ == '__main__':
    find_solutions(4)  #ищет долго, но находит )