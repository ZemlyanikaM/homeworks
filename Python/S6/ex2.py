# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

#list
import random
n =  random.randint(4, 10)
print(f'N = {n}')
# 
# было
# 
# list = []
# print(list)
# for i in range(0, n):
#     list.append(random.randint(-n,n))
# print(list)
# 
# стало
# 
list = [random.randint(-n,n) for i in range(0, n)]
print(list)

#file 
count = random.randint(2, (n//2))
pf = open('pos.txt', "w")
pf.write('')
pf.close()
for i in range(0, count):    
    with open('pos.txt', "a") as pf:
        pf.write(f'{random.randint(0,n-1)} \n')
#multiply
mult = 1
with open('pos.txt', "r") as pf:
    for line in pf:
        print(int(line), end = ' ')
        mult *=list[int(line)]
print(f'\n {mult}')

