# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

import random

num_dec = random.randint(0, 99)
print(f'Dec:{num_dec}')
num_bin = ""
while num_dec != 0:
    rd = str(num_dec % 2)
    num_bin = rd+num_bin
    num_dec //= 2
print(f'Bin:{num_bin}')
