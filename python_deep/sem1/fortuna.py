from random import randint
num = randint(0, 100)
attempt = 10
while attempt > 0:
    userNum = int(input("Enter a number: "))
    if userNum == num:
        print(f"You got it!")
    elif userNum > num:
        attempt -= 1
        print(f"Wrong! The {userNum} is bigger then magic num")
    else:
        print(f"Wrong! The {userNum} is lower then magic num")
        attempt -= 1