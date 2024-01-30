def byn_search(arr, find):
    low = 0
    hi = len(arr) - 1

    while low <= hi:
        middle = (low + hi) // 2
        middle_value = arr[middle]

        if middle_value == find:
            return middle
        elif middle_value < find:
            low = middle + 1
        else:
            hi = middle - 1
    return -1


if __name__ == '__main__':
    data = [1, 4, 9, 26, 45, 67, 76, 90, 101]
    print(byn_search(data, 67))
