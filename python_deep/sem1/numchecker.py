num = -1
while 0 > num or num > 100000:
    num = int(input("Enter a number 0 - 100000: "))


def is_prime(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


print(f'{num} is a prime number: {is_prime(num)}')
