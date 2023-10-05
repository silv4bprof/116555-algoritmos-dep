from random import randint

matrix = [
    [13, 32,  3],
    [14, 51,  6],
    [47,  8, 59]
]

menor = matrix[0][0]

for l in range(3):
    for c in range(3):
        print(f'Menor agora é: {menor}')
        print(f'{matrix[l][c]} é menor do que {menor}?')
        if matrix[l][c] < menor:
            print(f'{matrix[l][c]} é menor do que {menor}!')
            menor = matrix[l][c]
        else:
            print(f'{matrix[l][c]} NÃO é menor do que {menor}!')




# print('\nPREENCHENDO POSIÇÕES DA MATRIZ')
# for linha in range(3):
#     l = [0]*3
#     matrix.append(l)


# print('\nPREENCHENDO POSIÇÕES DA MATRIZ')
# for linha in range(3):
#     for coluna in range(3):
#         numero = int(input(f'Número para posição [{linha+1}, {coluna+1}]: '))
#         matrix[linha][coluna] = numero
