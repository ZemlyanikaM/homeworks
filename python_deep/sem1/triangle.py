print("Enter a lengths of a triangle's sides")
a = int(input("Enter a side A: "))
b = int(input("Enter a side B: "))
c = int(input("Enter a side B: "))

if a+b < c or b+c < a or a+c < b:
    print(f"a triangle with sides {a} , {b}, {c} cannot exist")
elif a == b == c:
    print("the equilateral triangle")
elif a == b or a == c or b == c:
    print("the isosceles triangle")
else:
    print(f"a triangle with sides {a} , {b}, {c} can exist")