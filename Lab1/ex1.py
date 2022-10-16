# Find The greatest common divisor of multiple numbers read from the console.
'''
aici ar trebui validat input ul, in rest e ok
'''
def gcd(x, y):
    if y == 0:
        return abs(x)
    else:
        return gcd(y, x % y)


def gcd_multiple_numbers(numbers):
    res = -1
    if len(numbers) > 0:
        res = numbers[0]
    for index in range(1, len(numbers)):
        res = gcd(res, numbers[index])
    return res


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    print(gcd_multiple_numbers(numbers))
