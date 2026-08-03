lista = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

numero = 1
for i in range(len(lista)):
    for j in range(len(lista[i])):
        lista[i][j] = numero
        numero += 1
        
for linha in lista:
    print(linha)
