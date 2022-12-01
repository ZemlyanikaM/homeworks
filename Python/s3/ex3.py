# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
#     - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19

import random

n = random.randint(3, 10)
nums = []
for i in range(0, n):
    nums.append(round((random.random()*10), 2))
print(nums)
max = nums[0] % 1
min = nums[0] % 1
for i in range(1, n):
    if max < nums[i] % 1:
        max = nums[i] % 1
    if min > nums[i] % 1:
        min = nums[i] % 1
diff = round((max % 1 - min % 1), 2)

print(round(min, 2), round(max, 2))
print(diff)
