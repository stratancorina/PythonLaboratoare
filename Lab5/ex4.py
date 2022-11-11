def my_function(*args, **kwargs):
    return [
               i for i in args
               if type(i) == dict and len(i) > 1 and max([0] + [len(x) for x in i.keys() if type(x) == str]) > 2
           ] + [
               i for i in kwargs.values()
               if type(i) == dict and len(i) > 1 and max([0] + [len(x) for x in i.keys() if type(x) == str]) > 2
           ]


if __name__ == '__main__':
    print(my_function(
        {1: 2, 3: 4, 5: 6},
        {'a': 5, 'b': 7, 'c': 'e'},
        {2: 3},
        [1, 2, 3],
        {'abc': 4, 'def': 5},
        3764,
        dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
        test={1: 1, 'test': True}
    ))