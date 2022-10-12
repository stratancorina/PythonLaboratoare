# Write a function that validates if a number is a palindrome.

if __name__ == '__main__':
    number = 1111
    number_to_string = str(number)
    if number_to_string == number_to_string[::-1]:
        print('Palindrom')
    else:
        print('Nu e palindrom')