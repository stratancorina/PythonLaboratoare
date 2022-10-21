# Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

# def prime_numbers(nrs)

def is_prime(n):
    for k in range(2, n):
        if (n % k) == 0:
            return False
    return True


if __name__ == '__main__':
    lst = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        if is_prime(ele):
            lst.append(ele)

    print("Prime numbers are: ")
    print(lst)
