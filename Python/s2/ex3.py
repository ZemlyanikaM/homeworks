# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
#     *Пример:*
#     - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
#     Необходимо сложить все значения словаря и вывести  сумму на экран.

import random
n = random.randint(1, 5)
dict = {}
sum =0
for i in range(1, n+1):
    dict[i]=(1 +(1/i))**i
    sum += dict[i]
print(dict)
print(sum)