import re
from typing import List


def ex_3(input_text: str, regex_list: List[str]) -> List[str]:
    match_list = []
    for i in regex_list:
        x = re.findall(i, input_text)
        for j in x:
            if j not in match_list:
                match_list.append(j)
    return match_list


if __name__ == '__main__':
    print(ex_3("text, ana, are mere", [r"\w\w\w", r"mere"]))