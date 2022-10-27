def comparing(d1, d2):
    res = all((d1.get(k) == v for k, v in d2.items()))
    print(res)


if __name__ == '__main__':
    x = {"a": 3, "b": 2}
    y = {"a": 2, "b": 3}
    comparing(x, y)
