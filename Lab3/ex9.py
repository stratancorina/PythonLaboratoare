def ex_9(*positions, **arguments):
    count = 0
    for element in arguments:
        if arguments[element] in positions:
            count += 1
    return count


if __name__ == '__main__':
    print(ex_9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
