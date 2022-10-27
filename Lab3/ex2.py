# Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
# characters in the character string and the values are the number of occurrences of that character in the given text.

def count_char(input_string: str) -> dict:
    characters_in_string = set(input_string)
    return dict([(x, input_string.count(x)) for x in characters_in_string])


if __name__ == '__main__':
    str = input()
    print(count_char(str))
