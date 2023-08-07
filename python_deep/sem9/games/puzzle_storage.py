"""
Puzzle storage
"""
__all__ = ['storage', "show_stat"]

from puzzle import puzzle

_data = {}


def storage(attempts: int = 3):
    puzzle_dict = {
        'Зимой и летом одним цветом': ['сосна', 'елка', 'ель'],
        'Висит груша, нельзя скушать': ['лампа', 'лампочка'],
    }
    for puzzle_text, answers in puzzle_dict.items():
        result = puzzle(puzzle_text, answers, attempts)
        add_stat(puzzle_text, result)
        print(result)


def add_stat(puzzle_text: str, attempt: int):
    _data.update({puzzle_text: attempt})


def show_stat():
    print('Статистика ответов: ')
    res = '\n'.join((f'Загадка: {puzzle_text}. {f"Угадана с {attempt} попытки." if attempt > 0 else "Не угадана."}' \
                     for puzzle_text, attempt in _data.items()))
    print(res)


if __name__ == '__main__':
    storage()
    show_stat()
