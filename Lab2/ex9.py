def ex9(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i):
                if matrix[k][j] >= matrix[i][j]:
                    result.append((i, j))
                    break
    return result


if __name__ == "__main__":
    matrice = [[1, 2, 3, 2, 1, 1],
              [2, 4, 4, 3, 7, 2],
              [5, 5, 2, 5, 6, 4],
              [6, 6, 7, 6, 7, 5]]

    print(ex9(matrice))
