# Реализовать функцию, которая на вход принимает строку с математическим выражением и выдает ответ. *, /, +, -

num = '1 + 2 * 3 / 2 - 3 + 14 / 2 + 2 * 3'
num = num.split()
print(num)
while len(num) > 1:
    while '*' in num or '/' in num :
        if num.count('*') > 0 and num.count('/') > 0:
            if num.index('/') > num.index('*'):
                num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
            else:
                num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
        else:
            if '*' in num:
                num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
            else:
                num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
    print(num)    
    while '+' in num or '-' in num :
        if num.count('+') > 0 and num.count('-') > 0:
                num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
                num.pop(num.index('+') + 1)
                num.pop(num.index('+'))
                num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
                num.pop(num.index('-') + 1)
                num.pop(num.index('-'))
        else:
            if '+' in num:
                num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
                num.pop(num.index('+') + 1)
                num.pop(num.index('+'))
            else:
                num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
                num.pop(num.index('-') + 1)
                num.pop(num.index('-'))
print(num)