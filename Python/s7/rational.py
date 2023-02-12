from logdata import logdata
from fractions import Fraction

def calcr(data):
    result = f'{data[0]} {data[1]} {data[2]} = '
    if data[1] == '+':
        result += str(Fraction(data[0])+Fraction(data[2]))
    elif data[1] == '-':
        result += str(Fraction(data[0])-Fraction(data[2]))
    elif data[1] == '*':
        result += str(Fraction(data[0])*Fraction(data[2]))
    elif data[1] == '/':
        result += str(Fraction(data[0])/Fraction(data[2]))
    logdata(result)
    return result