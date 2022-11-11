__doc__ = """
Write a module named utils.py that contains one function called process_item. The function will have one parameter, 
x, and will return the least prime number greater than x. When run, the module will request an input from the user, 
convert it to a number and it will display the output of the process_item function.
"""


def check_special_prime(sieve, num):
    while num:
        if not sieve[num]:
            return False
        num = int(num / 10)
    return True


def find_special_prime(n):
    sieve = [True for i in range(n * 10 + 1)]

    sieve[0] = False
    sieve[1] = False

    # sieve for finding the Primes
    for i in range(2, n * 10 + 1):
        if sieve[i]:
            for j in range(i * i, n * 10 + 1, i):
                sieve[j] = False
    while True:
        if check_special_prime(sieve, n):
            print(n)
            break

        else:
            n += 1


if __name__ == '__main__':
    try:
        x = int(input("Enter a number\n"))
        print(find_special_prime(x))
    except TypeError as e:
        print("Input is not integer", e)
    except Exception as e:
        print("Other error", e)
