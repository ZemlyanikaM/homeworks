from operator import itemgetter

my_diction = {'axe': 3, 'pot': 2, 'food': 4, 'water': 4, 'tent': 9, 'fire': 1, 'rope': 3, 'mat': 4, 'sleeping bag' : 5}
backpack = int(input("Enter backpack size: "))
weight = 0
current_weight = 0
print("Equipment in backpack", backpack, "kg:")

for things, value in dict(sorted(my_diction.items(), key=itemgetter(1))).items():
    weight += my_diction[things]
    if weight <= backpack:
        print(things, ' = ', value)
        current_weight += my_diction[things]

print("Total weight: ", current_weight)
