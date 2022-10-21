# Write a function that receives as parameters two lists a and b and returns:
# (a intersected with b, a reunited with b, a - b, b - a)

a = [1, 2, 3, 6, 7]
b = [5, 6, 7, 8, 9]


def operations_on_lists(m, n):
    print("Intersection: ")
    lst1 = [value for value in m if value in n]
    print(lst1)

    print("Union : ")
    lst2 = m + n
    print(lst2)

    print("a - b :")
    lst3 = {element for element in a if element not in b}
    print(lst3)

    print("b - a")
    lst4 = {element for element in b if element not in a}
    print(lst4)


if __name__ == '__main__':
    print(operations_on_lists(a, b))
