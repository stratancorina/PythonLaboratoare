# Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique
# elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve this
# objective).

def count_elements(lista):
    a = len(set(lista))
    b = len(lista) - a
    return a, b
    # return (len(set(lista)), len(lista) - len(set(lista)))


if __name__ == '__main__':
    elements = ["a", "b", "a", 1, 3, 2, 1]
    print(count_elements(elements))
