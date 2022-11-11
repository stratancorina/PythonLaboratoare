# Write a function that receives a list with integers as parameter that contains an equal number of even and odd
# numbers that are in no specific order. The function should return a list of pairs (tuples of 2 elements) of numbers
# (Xi, Yi) such that Xi is the i-th even number in the list and Yi is the i-th odd number "
import builtins


def arrange_numbers(li):
    a = []
    b = []
    for n in li:
        if n % 2 == 0:
            a.append(n)
        else:
            b.append(n)
    couples = list(zip(a, b))
    print(couples)


if __name__ == '__main__':
    arrange_numbers([1, 3, 5, 2, 8, 7, 4, 10, 9, 2])
