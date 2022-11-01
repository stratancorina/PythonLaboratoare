'''
aici lipseste recursivitatea si verificarea in functie de tipul valorilor si al valorilor din lista de valori a
cheilor. ideea era ca poti avea dictionare nested la adancimi mai mari in dictionare, iar ideea era ca pe masura ce
treci prin chei, daca toate cheile sunt aceleasi peste tot, treci la valorile din chei, daca valorile din chei au tip
diferit / valori diferite atunci te opresti, iar daca dai peste dictionare ar trebui sa apelezi din nou aceeasi functie
si tot asa
'''
def comparing(d1, d2):
    res = all((d1.get(k) == v for k, v in d2.items()))
    print(res)


if __name__ == '__main__':
    x = {"a": 3, "b": 2}
    y = {"a": 2, "b": 3}
    comparing(x, y)
