from logdata import logdata

def calcc(data):
    a = complex(int(data[0]),int(data[1]))
    b = complex(int(data[3]),int(data[4]))
    result = f'{a} {data[2]} {b} = '
    if data[2] == '+':
        result += str(a+b)
    elif data[2] == '-':
        result += str(a-b)
    elif data[2] == '*':
        result += str(a*b)
    elif data[2] == '/':
        result += str(a/b)
    logdata(result)
    return result