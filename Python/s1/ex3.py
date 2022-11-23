import random


def which_quarter(x, y):
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    else:
        print(4)


x = 0
y = 0
while (x == 0 or y == 0):
    x = random.randint(-99, 99)
    y = random.randint(-99, 99)
print(x, y)
which_quarter(x, y)
