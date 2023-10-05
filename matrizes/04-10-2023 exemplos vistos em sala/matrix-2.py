mat = []

l = int(input('Quantidade de linhas: '))
c = int(input('Quantidade de colunas: '))

for i in range(l):
    linha = [0]*c
    mat.append(linha)

print('\n FORMA FEIA')
for i in range(l):
    print(mat[i])

print('\nFORMA BONITA')
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(f'{mat[i][j]}', end=' ')
    print()

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i == j:
            mat[i][j] = 1

print('\nFORMA BONITA')
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(f'{mat[i][j]}', end=' ')
    print()