# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

data = ['A', 'A', 'd', 'vv', 'vv', '5', '5', 'w', 'w', '-4', '12']
c_data = []
e_data = []


def rle_code(data):
    row = 1
    for i in range(0, len(data)-1):
        if data[i+1] == data[i]:
            row += 1
            if i == len(data)-2:
                c_data.append((row, data[i]))
        else:
            c_data.append((row, data[i]))
            row = 1
            if i == len(data)-2:
                c_data.append((row, data[i+1]))
    return c_data


def rle_encode(c_data):
    for i in c_data:
        count = i[0]
        for j in range(0, count):
            e_data.append(i[1])
    return e_data


print(data)
print(rle_code(data))
print(rle_encode(c_data))
