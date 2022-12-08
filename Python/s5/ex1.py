# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
SWEET = 2021
MAX = 28
P1 = "Игрок 1"
P2 = "Игрок 2"
B1 = "Бот"
B2 = "Бот 2"
candy = SWEET
counts = []


def p_move(candy, player):
    print(f'Конфет на столе: {candy}')
    print(f'Берёт конфеты {player}')
    if candy < MAX:
        max = candy
    else:
        max = MAX
    check = False
    while check == False:
        count = int(input(f'Сколько конфет берешь? (Максимум - {max}) '))
        if count > max:
            print(f'Не корректный ввод. Максимум {max} конфет')
        else:
            check = True
    candy -= count
    counts.insert(0, count)
    return candy


def b_move(candy, player):
    print(f'Конфет на столе: {candy}')
    if candy < MAX:
        count = candy
    else:
        max = MAX
        count = random.randint(1, max)
    print(f'{player} взял {count} конфет')
    candy -= count
    counts.insert(0, count)
    return candy


def b2_move(candy, player):
    print(f'Конфет на столе: {candy}')
    if candy == SWEET:
        count = SWEET % (MAX+1)
    elif candy < MAX:
        count = candy
    else:
        count = MAX+1 - counts[0]
    candy -= count
    print(f'{player} взял {count} конфет')
    return candy


print('Выбери режим игры:')
print('0 - Два игрока')
print('1 - Игра против компьютера')
print('2 - Two bots')
print('3 - Bot God Mode')
mode = int(input())
p = True
while candy > 0:
    if mode == 0:
        if p == True:
            player = P1
        else:
            player = P2
        candy = p_move(candy, player)
        p = not p
    elif mode == 1:
        if p == True:
            player = P1
            candy = p_move(candy, player)
        else:
            player = B1
            candy = b_move(candy, player)
        p = not p
    elif mode == 2:
        if p == True:
            player = B1
        else:
            player = B2
        candy = b_move(candy, player)
        p = not p
    else:
        print()
        if p == True:
            player = B2
            candy = b2_move(candy, player)
        else:
            player = B1
            candy = b_move(candy, player)
        p = not p


p = not p


print(f'Игра закончена, победитель: {player}')
