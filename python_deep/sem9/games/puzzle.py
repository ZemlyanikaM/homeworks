"""
Puzzle game
"""
__all__ = ['puzzle']


def puzzle(puzzle_text: str, answers: list[str], attempt: int) -> int:
    print(puzzle_text)
    i = 1
    while i <= attempt:
        user_answer = input("Enter an answer: ")
        if user_answer in answers:
            return i
        else:
            i += 1
            if i <= attempt:
                print(f"Wrong! Try again. You have {attempt - i + 1} attempts")
            else:
                return 0


if __name__ == '__main__':
    print(puzzle("Зимой и летом одним цветом", ['сосна', 'елка', 'ель'], 3))
