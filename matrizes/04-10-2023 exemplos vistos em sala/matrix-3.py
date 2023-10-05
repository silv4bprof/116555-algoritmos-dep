mat1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
mat2 = [[1, 1, 1], [1, 1, 1], [3, 3, 3]]

mat3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(mat1)):
    for j in range(len(mat1[i])):
        mat3[i][j] = mat1[i][j] + mat2[i][j]

print(mat3)
