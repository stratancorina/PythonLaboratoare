# Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function
# will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the
# first number that is found.

def first_number(text):
    res = ''
    for i in range(0, len(text)):
        if text[i].isnumeric():
            for j in range(i, len(text)):
                if text[j].isnumeric():
                    res += text[j]
                else:
                    return res


if __name__ == '__main__':
    string = input()
    print(first_number(string))
