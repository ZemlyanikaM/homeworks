import random


def show_coord(q):
    if q == 1:
        print(f"quarter {q}. x > 0, y > 0")
    elif q == 2:
        print(f"quarter {q}. x < 0, y > 0")
    elif q == 3:
        print(f"quarter {q}. x < 0, y < 0")
    else:
        print(f"quarter {q}. x > 0, y < 0")


quarter = random.randint(1, 4)
show_coord(quarter)
