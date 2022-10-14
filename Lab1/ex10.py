# Write a function that counts how many words exists in a text. A text is considered to be form out of words that
# are separated by only ONE space. For example: "I have Python exam" has 4 words.

if __name__ == '__main__':
    string = input()
    print(len(list(string.split())))
