# Вычислить число Пи c заданной точностью d
# Пример:
#     - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10

import math
d = 0.000001
print(d)
count = 0
while d < 1:
    count += 1
    d *= 10
p = str(math.pi).split('.')
pd = p[0] + "." + p[1][:count]
print(pd)
