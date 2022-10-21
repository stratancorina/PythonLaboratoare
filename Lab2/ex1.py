# Write a function to return a list of the first n numbers in the Fibonacci string.
def fibonacci_numbers(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        # printing fibonacci numbers
        return fibonacci_numbers(num - 2) + fibonacci_numbers(num - 1)


if __name__ == '__main__':
    n = input()
    for i in range(0, int(n)):
        print(fibonacci_numbers(i), end=" ")
