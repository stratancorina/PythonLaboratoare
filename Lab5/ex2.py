anonymous_function = lambda *args, **kwargs: sum(kwargs.values())


def my_function(*args, **kwargs):
    return sum(kwargs.values())


if __name__ == '__main__':
    result_1 = anonymous_function(2, 3, d=2, e=3, a=1)
    result_2 = my_function(2, 3, d=2, e=3, a=1)
    print(result_1, result_2)