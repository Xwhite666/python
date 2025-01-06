
n = 7
matrix = [[0] * n for _ in range(n)]


for i in range(n):
    for j in range(n):

        if j % 2 == 0:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0


for row in matrix:
    print(row)
