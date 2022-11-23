for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(x, y, z)
            print(-(x or y or z) == (-x or -y or -z))
