# Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.
# (Не используя библиотеки связанные с рандомом)

import time
def get_seed():
    value = str(time.time())
    seed = int(value[len(value)-1])
    return seed
p_num = ((get_seed()*get_seed()) // get_seed())%10

print(p_num)

