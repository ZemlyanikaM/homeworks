import random
ax = random.randint(1, 99)
ay = random.randint(1, 99)
bx = random.randint(1, 99)
by = random.randint(1, 99)
ab = ((bx-ax)**2 + (by - ay)**2)**0.5
print(f"A({ax},{ay}), B({bx},{by}). AB={round(ab, 3)}")
