# Write a script that receives two strings and prints the number of occurrences of the first string in the second.
'''
aici ar trebui sa tratezi si cazuri de genul first_string = 'aaa', second_string = 'aaaaa' -> 3 aparitii, nu 1
'''
if __name__ == '__main__':
    first_string = input()
    second_string = input()
    print(second_string.count(first_string))

    """
    first_string = "ana"
    second_string = "ana mananca mere"
    print(second_string.count(first_string))
    """
