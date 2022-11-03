import os
from pathlib import Path


def last_characters(my_path):
    if Path(my_path).is_file():
        return open(my_path, "r").read()[-21:]
    elif Path(my_path).is_dir():
        list = []
        count = []
        for files in os.listdir(my_path):
            extension = os.path.splitext(files)[1]
            if extension not in list:
                list.append(extension)
                count.append(1)
            else:
                count[list.index(extension)] += 1
        tuple_list_count = tuple(zip(list, count))
        tuple_list_count = sorted(tuple_list_count, key=lambda x: x[1], reverse=True)
        return tuple_list_count


if __name__ == '__main__':
    print(last_characters(".\exemple\\buna-ziua.txt"))
    print(last_characters(".\exemple"))
