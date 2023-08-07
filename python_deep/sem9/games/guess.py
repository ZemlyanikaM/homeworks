"""Guess the number game"""
__all__ = ['puzzle_guess']


from guess_deco import deco as validate
from guess_save2json import save2json
from guess_param_deco import param_deco as trials


@trials(3)
@validate
@save2json
def puzzle_guess(num: int, attempts: int):
    """Guess the number game"""
    for i in range(1, attempts + 1):
        print(f'Attempt: {i}')
        user_answer = int(input("Enter a number: "))
        if user_answer == num:
            print('You won!')
            return
        elif user_answer > num:
            print(f'The {user_answer} is bigger.')
        else:
            print(f'The {user_answer} is smaller.')


if __name__ == '__main__':
    puzzle_guess(15, 3)
    print(f'{puzzle_guess.__name__ = }')
    print(f'{puzzle_guess.__doc__ = }')
