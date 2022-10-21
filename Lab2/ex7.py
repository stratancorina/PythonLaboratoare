numbers = [10, 11, 23, 333, 44, 90]


def find(nums):
    palindromes = []
    result1 = 0
    for n in nums:
        k = str(n)
        if k == k[::-1]:
            result1 = result1 + 1
            palindromes.append(int(k))
            
    result2 = max(palindromes)
    return result1, result2


if __name__ == '__main__':
    print(find(numbers))
