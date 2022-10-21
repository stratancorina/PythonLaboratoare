def ex8(x=1, li=None, flag=True):  # numarul x, lista l
    if li is None:
        li = []
    return [list(filter(lambda c: (ord(c) % x == 0) == flag, s)) for s in li]


# Returneaza o lista de liste. Fiecare in lista returnata contine toate elementele din li
# care au valoare la indexul specificat de x, adica nr par in ascii

if __name__ == '__main__':
    print(ex8(3, ["test", "hello", "lab002"], False))
