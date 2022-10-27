def ex_8(mapping):
    visited = {}
    res = []
    current = mapping['start']
    while True:
        if current in visited:
            return res
        res.append(current)
        visited[current] = 1
        current = mapping[current]


if __name__ == '__main__':
    print(ex_8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
