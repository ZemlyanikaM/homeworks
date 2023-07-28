def args_to_dict(**params):
    result = {}
    for key, value in params.items():
        try:
            hash(key)
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result


print(args_to_dict(time='15-00-00', day='friday', month=7,
                   hours=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                   summer={6: 'June', 7: 'July', 8: 'August'}))

