started_list = [5, 7, 3, 1, 1, 3, 5, 9, 2, 1, 7]

my_set = set()

for item in started_list:
    if started_list.count(item) > 1:
        my_set.add(item)
print(list(my_set))
