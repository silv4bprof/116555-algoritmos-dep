matrix = [
    ['a', 'a', 'a'],
    ['b', 'b', 'b'],
    ['c', 'c', 'c']
]

print('\nEXIBINDO LINHA A LINHA')
for linha in range(3):
    for coluna in range(3):
        print(matrix[linha][coluna], end=' ')
    print()

print('\nEXIBINDO COLUNA A COLUNA')
for linha in range(3):
    for coluna in range(3):
        print(matrix[coluna][linha], end=' ')
    print()

print('\nPREENCHENDO POSIÇÕES DA MATRIZ')
for linha in range(3):
    for coluna in range(3):
        numero = int(input(f'Número para posição [{linha}, {coluna}]: '))
        matrix[linha][coluna] = numero

# exibindo matriz preenchida
for linha in range(3):
    for coluna in range(3):
        print(matrix[linha][coluna], end=' ')
    print()

print('\nTROCANDO VALORES ATRAVÉS DAS POSIÇÕES DE LINHA E COLUNA')
linha = int(input('Digite a linha da tabela que deseja acessar: '))
linha = int(input('Digite a coluna da tabela que deseja acessar: '))
valor = int(input('Digite o novo valor: '))

matrix[linha][coluna] = valor

# exibindo matriz preenchida
for linha in range(3):
    for coluna in range(3):
        print(matrix[linha][coluna], end=' ')
    print()

print('EXEMPLO: CAIXA REGISTRADORA LISTA DE LISTAS')
registradora = [
    # codigo - nome do produto - quantidade
    [1, 'Macarrão', 20],
    [2, 'Arroz', 20],
    [3, 'Milho', 20]
]

codigos = []
for i in registradora:
    codigos.append(i[0])
print(codigos)

while True:
    #exibindo produtos
    print('\nPRODUTOS (COMEÇO)')
    for i in registradora:
        print(f'Código: {i[0]}', end=' ')
        print(f'Nome: {i[1]}', end=' ')
        print(f'Quantidade: {i[2]}', end='\n')

    num_prod = int(input('Qual produto deseja vender (0 para sair): '))
    if num_prod == 0:
        break
    elif num_prod not in codigos:
        print('Produto não existe ... tente novamente.')
        continue
    else:
        for prod in registradora:
            if num_prod == prod[0]:
                prod[2] -= 1

print('\nPRODUTOS (FINAL)')
for i in registradora:
    print(f'Código: {i[0]}', end=' ')
    print(f'Nome: {i[1]}', end=' ')
    print(f'Quantidade: {i[2]}', end=' ')
    print()