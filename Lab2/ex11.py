# 11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the
#     tuple.

from typing import List


def ex_11(input_list: List[tuple]) -> List[tuple]:
    input_list.sort(key=lambda x: x[1][2])
    return input_list


if __name__ == '__main__':
    print(ex_11([('abc', 'bcd'), ('abc', 'zza')]))
