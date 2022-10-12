# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

if __name__ == '__main__':
    first_string = input()
    res = ''
    for i in first_string:
        if i.isupper():
            if len(res) > 0 and res[len(res) - 1].isalpha():
                res += '_'
        res += i.lower()

    print(res)