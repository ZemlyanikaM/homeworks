"""
check_year
"""
__all__ = ['check_date']

from sys import argv

def if_leap(year: int) -> bool:
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def check_date(str_date: str) -> bool:
    day, month, year = map(int, str_date.split('.'))
    if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999):
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if month == 2 and if_leap(year) and day > 29:
        return False
    if month == 2 and not if_leap(year) and day > 28:
        return False
    return True


if __name__ == '__main__':
    input_date = argv[1]
    print(check_date(input_date))