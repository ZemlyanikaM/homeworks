from guess import puzzle_guess
from puzzle_storage import storage as puzzle
from puzzle_storage import show_stat

if __name__ == '__main__':
    puzzle_guess(25, 3)
    puzzle(3)
    show_stat()
