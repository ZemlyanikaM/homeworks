ALPHABET = {
    0: "0", 1: "1", 2: "2", 3: "3",
    4: "4", 5: "5", 6: "6", 7: "7",
    8: "8", 9: "9", 10: "a", 11: "b",
    12: "c", 13: "d", 14: "e", 15: "f"}
HEX = 16


def user_input() -> int:
    n = input("Enter a number: ")
    return int(n)


def dec_to_hex(num: int) -> str:
    hex_num: str = ''
    while num > 0:
        hex_num = ALPHABET.get(num % HEX) + hex_num
        num //= HEX
    return hex_num


num: int = user_input()
print(dec_to_hex(num))
print(hex(num))
