# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

import random
n = random.randint(3, 10)
nums = []
for i in range(0, n):
    nums.append(random.randint(-10, 10))
pairs = []
print(nums)
if n % 2 == 0:
    for i in range(0, n//2):
        pairs.append(nums[i]*nums[n-i-1])
else:
    for i in range(0, n//2+1):
        pairs.append(nums[i]*nums[n-1-i])

print(pairs)
