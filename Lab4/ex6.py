from ex5 import *
from pathlib import Path



def check_path_6(path, callback: callable(Path)):
    if os.path.isdir(path):
        return "dir"
    elif os.path.isfile(path):
        return "file"
    else:
         callback(path + ": is not a valid path to file or directory")

def lists_6(target, to_search, callback: callable(Path)):
    check = check_path_6(target, callback)
    if check == "file":
        if search_string_in_file(target, to_search) ==True:
            return [target]
    elif check == "dir":
        list = []
        for file in os.listdir(target):
            try:
                if check_path_6(file) == "dir":
                    list +=(lists(file, to_search))
                elif check_path_6(file) == "file":
                    if search_string_in_file(file, to_search) == True:
                        list.append(file)
            except Exception as e:
                callback(e)
        return list


if __name__ == '__main__':
    print(lists_6(".\exemple\\buna-ziua.txt", 'Lorem Ipsum', callable(Path)))
