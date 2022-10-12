# Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format
# is 00011000, meaning 2 bits with value "1"

if __name__ == '__main__':
    number = int(input())
    res = 0
    for i in range(0, 32):
        if number & (1 << i):
            res += 1
    print(res)
