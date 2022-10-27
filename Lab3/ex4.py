from xml.etree import ElementTree


def build_xml_element(tag: str, content: str, **elements) -> str:
    return "<{}{}>{}</{}>".format(
        tag,
        '\ '.join(["{}={}".format(key, value) for key, value in elements.items()]),
        content,
        tag
    )


if __name__ == '__main__':
    print(build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))
    # the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

    # o alternativa mai slaba
    xml = ElementTree.Element("a", href=" http://python.org ", _class=" my-link ", id=" someid ")
    xml_str = ElementTree.tostring(xml).decode()
    print(xml_str)
