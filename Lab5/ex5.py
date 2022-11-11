import re


def my_function(list):
    return re.findall(r"[0-9]+\.?[0-9]*", str(list))


if __name__ == '__main__':
    list1 = [1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]
    print(my_function(list1))
