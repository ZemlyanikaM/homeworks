# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import random
n = random.randint(2, 100)
print(n)
i = 2
pm = []
while n != 1:
    if n % i == 0:
        pm.append(i)
        n = n // i
    else:
        i += 1
print(pm)
