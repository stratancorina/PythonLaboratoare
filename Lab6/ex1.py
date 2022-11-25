# Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of
# lpha-numeric characters.
import re
from typing import List


def extract_words(input_text: str) -> List[str]:
    return re.findall(r"[a-zA-Z0-9]+", input_text)


if __name__ == '__main__':
    print(extract_words("text, ana, are mere"))