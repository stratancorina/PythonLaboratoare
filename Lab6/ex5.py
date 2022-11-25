import re
from typing import List


def ex_5(path: str, attributes: dict) -> List[str]:
    match_list = []
    with open(path, "r") as file:
        xml_data = file.read()
        search_string = r"(<(\w+) [^>]*(" + r"|".join(
            ["{key}=\"{value}\"".format(key=key, value=value) for key, value in attributes.items()]
        ) + r")[^>]*>[^(<\2>)]*</\2>)"
        print(search_string)
        match_list += [x[0] for x in re.findall(search_string, xml_data)]
    return match_list


if __name__ == '__main__':
    print(ex_5("example.xml", {"class": "url", "name": "url-form", "data-id": "item"}))