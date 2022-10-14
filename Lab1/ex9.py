# Write a functions that determine the most common letter in a string. For example if the string is "an apple
# is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered.
# Casing should not be considered "A" and "a" represent the same character.

def print_the_most_common_characters(string):
    my_map = {}

    for i in range(0, len(string)):
        if string[i].isalpha():
            if string[i].lower() in my_map:
                my_map[string[i].lower()] += 1
            else:
                my_map[string[i].lower()] = 1

    max_frequency = max(my_map.values())
    for key in my_map:
        if my_map[key] == max_frequency:
            print(key)


if __name__ == '__main__':
    string = input()
    print_the_most_common_characters(string)