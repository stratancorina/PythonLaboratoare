import re
from typing import List


def ex_2(regex: str, input_text: str, x: int) -> List[str]:
    return [i for i in re.findall(regex, input_text) if len(i) == x]


if __name__ == '__main__':
    print(ex_2(r"\w+", "text, ana, are mere", 3))