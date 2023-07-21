import math
from fractions import Fraction


def user_input():
    data = input("Enter two fractions (a/b c/d: ")
    f1, f2 = data.split()
    return f1, f2


def cat_fraction(n: int, d: int):
    if n > d:
        k = n
    else:
        k = d
    while k != 1:
        if n % k == 0 and d % k == 0:
            return str(n // k) + "/" + str(d // k)
        else:
            k -= 1
    return str(n) + "/" + str(d)


def fraction_sum(f1: str, f2: str) -> str:
    frac1 = f1.split("/")
    frac2 = f2.split("/")
    lcm = math.lcm(int(frac1[1]), int(frac2[1]))
    nf1 = int(lcm / int(frac1[1])) * int(frac1[0])
    nf2 = int(lcm / int(frac2[1])) * int(frac2[0])
    return cat_fraction(nf1 + nf2, lcm)


def fraction_mult(f1: str, f2: str) -> str:
    frac1 = f1.split("/")
    frac2 = f2.split("/")
    return cat_fraction(int(frac1[0]) * int(frac2[0]), int(frac1[1]) * int(frac2[1]))


f1, f2 = user_input()

print(fraction_sum(f1, f2))
print(Fraction(int(f1.split("/")[0]), int(f1.split("/")[1])) + Fraction(int(f2.split("/")[0]), int(f2.split("/")[1])))
print(fraction_mult(f1, f2))
print(Fraction(int(f1.split("/")[0]), int(f1.split("/")[1])) * Fraction(int(f2.split("/")[0]), int(f2.split("/")[1])))
