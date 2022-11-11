vowels = "AEIOUaeiou"
string = "Programming in Python is fun"


def func1(string):
    return [x for x in string if x in vowels]


def func2(string):
    return list((filter(lambda letter: letter in vowels, string)))


def func3(string):
    newlist = [v for v in string if v in vowels]
    return newlist


if __name__ == '__main__':
    print(func1(string))
    print(func2(string))
    print(func3(string))
