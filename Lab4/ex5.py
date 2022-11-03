import os


def check_path(path):
    if os.path.isdir(path):
        return "dir"
    elif os.path.isfile(path):
        return "file"
    else:
        raise ValueError(path + ": is not a valid path to file or directory")


def search_string_in_file(file, string):
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        if string in line:
            return True
    return False


def lists(target, to_search):
    check = check_path(target)
    if check == "file":
        if search_string_in_file(target, to_search):
            return [target]
    elif check == "dir":
        list = []
        for file in os.listdir(target):
            if check_path(file) == "dir":
                list += (lists(file, to_search))
            elif check_path(file) == "file":
                if search_string_in_file(file, to_search):
                    list.append(file)
        return list


if __name__ == '__main__':
    print(lists(".\exemple\\buna-ziua.txt", 'Lorem Ipsum'))
    print(lists("target","text"))
