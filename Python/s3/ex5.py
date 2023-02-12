# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import random
k = random.randint(3, 10)
nums = []


def fib(k):
    nums.append(0)
    if k == 0:
        return nums
    nums.append(1)
    if k == 1:
        return nums
    else:
        for i in range(2, k+1):
            nums.append(nums[i-2]+nums[i-1])
    return nums


def nfib(k):
    if k == 0:
        return nums
    nums.insert(0, 1)
    if k == 1:
        return nums
    else:
        for i in range(2, k+1):
            nums.insert(0, nums[1]-nums[0])
    return (nums)


fib(k)
nfib(k)
print(k)
print(nums)
