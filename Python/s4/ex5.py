# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*
# 2*x^5 + 2*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0

s1 = '2*x^5 + 2*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0'
s2 = '2*x^5 + 2*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0'

f1 = s1.split()
f2 = s2.split()
result = []
s3 = ''
for i in range(0, len(f1)):
    if f1[i][0].isdigit and f2[i][0].isdigit and f1[i][0] != '+' and f2[i][0] != '+' and f1[i][0] != '=' and f2[i][0] != '=':
        result.append(f'{int(f1[i][0])+int(f2[i][0])}{f1[i][1:]}')
    else:
        result.append(f1[i])
for i in result:
    s3 += i + ' '
with open('ex4_file2.txt', 'w') as data:
    data.write(s3)
print(s1)
print(s2)
print(s3)
