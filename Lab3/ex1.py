# 1.Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a
# intersected with b, a reunited with b, a - b, b - a)

def operations_on_sets(m, n):
    print("Intersection : ")
    i = m & n
    print(i)

    print("Union : ")
    u = m | n
    print(u)

    print("a - b :")
    d1 = m - n
    print(d1)

    print("b - a")
    d2 = n - m
    print(d2)


if __name__ == '__main__':
    a = {1, 2, 3, 6, 7}
    b = {5, 6, 7, 8, 9}
    print(operations_on_sets(a, b))