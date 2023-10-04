cd ..import argparse
from matrix import Matrix, logger


def str2matrix(in_args: list[str] = None) -> list[float]:
    if len(in_args) == 1:
        j = 0
    else:
        j = 1
    m_1 = []
    m_2 = []
    in_args[j].append(' ')
    for i in in_args[j]:
        if i == ' ':
            m_2.append(list(m_1))
            m_1.clear()
        else:
            m_1.append(float(i))
    return m_2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Addition, Multiplication and Comparison of matrices")
    parser.add_argument('-m_1', type=list, action='append',
                        default=[['0', '0', '0', ' ', '0', '0', '0', ' ', '0', '0', '0', ' ', '0', '0', '0']])
    parser.add_argument('-m_2', type=list, action='append',
                        default=[['0', '0', '0', ' ', '0', '0', '0', ' ', '0', '0', '0', ' ', '0', '0', '0']])
    parser.add_argument('-operation', type=str, default='+')
    args = parser.parse_args()

    m_1 = str2matrix(args.m_1)
    m_2 = str2matrix(args.m_2)

    if args.operation == '+':
        print(f'Addition: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) + Matrix(m_2)} '))
    elif args.operation == '*':
        print(f'Multiplication: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) * Matrix(m_2)} '))
    elif args.operation == '=':
        print(f'Comparison: {m_1} {args.operation} {m_2} : ', (f'{Matrix(m_1) == Matrix(m_2)} '))
    else:
        logger.error(f'The operation {args.operation} is not support! Use +, * or =')
        print(f'The operation {args.operation} is not support! Use +, * or =')

# python3 t_matrix.py -m_1='1 2 3' -m_2='4 5 6'
# python3 t_matrix.py -m_1='1 2 3' -m_2='4 5 6' -operation='='
# python3 t_matrix.py -m_1='1 2 3' -m_2='4 5 6' -operation='^'



