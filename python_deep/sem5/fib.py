num = int(input('Enter a number: '))


def fib(n):
    n1, n2 = 0, 1
    for _ in range(n):
        yield n1
        n1, n2 = n2, n1 + n2


print(list(fib(num)))
