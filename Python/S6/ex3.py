# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# было
# 
# import random
# n = random.randint(3, 10)
# nums = []
# sum_odds_i = 0 
# for i in range(0, n):
#     nums.append(random.randint(-10, 10))
#     if i % 2 != 0:
#         sum_odds_i += nums[i]
# print(sum_odds_i)
# стало
# 
sum_odds_i = 0
nums = [2, 3, 5, 9, 3]
def sum(x):
    global sum_odds_i
    sum_odds_i +=x
nums = list(map(sum, [nums[i] for i in range(len(nums)) if i % 2 !=0]))
print(sum_odds_i)
