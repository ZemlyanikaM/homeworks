# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import random
def fact(num):
    f = 1
    for i in range(1, num+1):
        f *= i
    return f
n = random.randint(1, 10)
print(n)
mults = []
for i in range (1, n+1):
   mults.append(fact(i)) 
print(mults)


