import os
import re
from typing import List


def ex_8(path: str, regex: str) -> List[str]:
    match_list = []
    try:
        for root, d, f in os.walk(path):
            for i in f:
                file_path = os.path.join(root, i)
                bool_1 = re.match(regex, file_path)
                bool_2 = re.match(regex, open(file_path, "r").read())
                if bool_1 and bool_2:
                    match_list.append(">>" + file_path)
                elif bool_1 or bool_2:
                    match_list.append(file_path)
    except Exception as e:
        SystemError(e)
    return match_list


if __name__ == '__main__':
    print(ex_8(".", ".*example.*"))
