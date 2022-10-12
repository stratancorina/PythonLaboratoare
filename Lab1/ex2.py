# Write a script that calculates how many vowels are in a string.


def number_of_vowels(string):
    vowels = 'aeiou'
    res = 0
    for i in string:
        if i in vowels:
            res += 1
    return res


if __name__ == '__main__':
    print(number_of_vowels('bunaziua'))
