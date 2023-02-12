# Создайте программу для игры в ""Крестики-нолики"".

P1 = 'Игрок 1'
P2 = 'Игрок 2'
M = 'Выбери поле: '
p = False
empty = {1, 2, 3, 4, 5, 6, 7, 8, 9}
field = [[' 1 ', ' 2 ', ' 3 '], [' 4 ', ' 5 ', ' 6 '], [' 7 ', ' 8 ', ' 9 ']]
winner = False


def p_field(field):
    for i in field:
        print(i)


def move():
    check = True
    while (check == True):
        move = int(input(M))
        if not move in empty:
            print('Не корректное поле, выбери свободное поле')
        else:
            check = False
    empty.remove(move)

    return move


def get_field(f):
    coord = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
    }
    return coord.get(f)


while winner == False:

    if not (field[0][0] == field[0][1] == field[0][2] or field[1][0] == field[1][1] == field[1][2] or field[2][0] == field[2][1] == field[2][2] or
            field[0][0] == field[1][0] == field[2][0] or field[0][1] == field[1][1] == field[2][1] or field[0][2] == field[1][2] == field[2][2] or
            field[0][0] == field[1][1] == field[2][2] or field[2][0] == field[1][1] == field[0][2]) and len(empty) > 0:
        if p == True:
            player = P2
        else:
            player = P1
        p_field(field)
        print(f'Ходит {player}.')
        f = move()
        co = get_field(f)
        if player == P1:
            field[co[0]][co[1]] = ' O '
        else:
            field[co[0]][co[1]] = ' X '
        p = not p
    elif len(empty) == 0:
        print("Победителя нет. Ничья.")
        winner = True
    else:
        p_field(field)
        print(f'{player} выиграл')
        winner = True
