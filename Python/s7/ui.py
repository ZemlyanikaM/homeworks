def ch_mode():
    while True:
        mode = input("Выбери режим калькулятора (0 - комплексные числа, 1 - рациональные числа):")
        if mode == '0' or mode == '1':
            break
        else:
            print('Ошибка ввода! Выбери 0 и или 1')
    return int(mode)


#тут тоже можно проверку ввода сделать, но лень )
def input_c():
    cplx = []
    cplx.append(input('Введи реальную часть первого комплексного числа: '))
    cplx.append(input('Введи мнимую часть первого комплексного числа: '))
    cplx.append(input('Введи действие ( +, -, * или / )'))
    cplx.append(input('Введи реальную часть второго комплексного числа: '))
    cplx.append(input('Введи мнимую часть второго комплексного числа: '))
    return cplx

def input_r():
    frac = []
    frac.append(input('Введи первую дробь (в формате 1/2, 3/5, 23/39, ...)'))
    frac.append(input('Введи действие ( +, -, * или / )'))
    frac.append(input('Введи вторую дробь (в формате 1/2, 3/5, 23/39, ...)'))
    return frac

def outp(result):
    print(result)

