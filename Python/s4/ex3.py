# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

import random
n = random.randint(5, 15)
col = [random.randint(1, 10) for i in range(1, n)]
print(col)
uniq = [col[i] for i in range(0, n-1) if col.count(col[i]) == 1]
print(uniq)
