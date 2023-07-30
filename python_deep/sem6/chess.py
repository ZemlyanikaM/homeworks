"""
8 queens
"""
__all__ = ['check_the_board']


def check_the_board(arrangement: list[list[int]]) -> bool:
    board = 8
    x = []
    y = []

    for i in range(board):
        x.append(arrangement[i][0])
        y.append(arrangement[i][1])
    is_beat = False
    for i in range(board):
        for j in range(i + 1, board):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                is_beat = True
    if is_beat:
        return False
    else:
        return True


if __name__ == '__main__':
    print(check_the_board([[3, 3], [6, 5], [4, 8], [2, 7], [8, 6], [7, 1], [5, 2], [1, 4]]))

#[[2, 6], [1, 3], [7, 7], [3, 4], [4, 2], [8, 1], [5, 8], [6, 5]]