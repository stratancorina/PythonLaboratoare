# Write a function that receives as parameter
# a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0

def zero(mat, n, m):
    for i in range(n):
        for j in range(m):
            # right and left diagonal condition
            if i == j or (i + j + 1) == n:
                mat[i][j] = 0

    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print()


if __name__ == '__main__':
    n = int(input("Select the number of rows and cols:"))
    m = n
    matrix = []

    for r in range(n):
        a = []
        for c in range(m):
            a.append(int(input()))
        matrix.append(a)

    for r in range(n):
        for c in range(m):
            print(matrix[r][c], end=" ")
        print()

    print("The matrix with 0 on diagonals is:")
    print(zero(matrix, n, m))
