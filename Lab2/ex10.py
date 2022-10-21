# Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple
# contains the first items in the lists, the second element contains the items on the position 2 in the lists,
# etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].

def combinat(lists):
    z = list(zip(lists[0], lists[1], lists[2], lists[3]))
    return z


if __name__ == '__main__':
    list1 = [3, 2, 1]
    list2 = ["ana", "maria", "alina"]
    list3 = ["ion", "andrei", "alex"]
    list4 = ["franta", "spania", "danemarca"]

    liste = [list1, list2, list3, list4]

    print(combinat(liste))
