# Напиши программу, которая на вход принимает вещественное число и выводит сумму входящих в него цифр

import random
n = str(round(random.uniform(0, 20), 5))
sum = 0
for i in n:
    if i!='.':
        sum += int(i)
print(n)
print(sum)