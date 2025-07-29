n = int(input())
notas = int(input())

matriz = []
medias = []

for i in range(n):
    lista = []
    lista = list(map(int,input().split()))
    matriz.append(lista)

for i in range(n):
    for k in range(notas-1):
        print(matriz[i][k], end= " ")
    print(matriz[i][k+1])

maior = -9999

for i in range(n):
    soma = 0
    for k in range(notas):
        soma += matriz[i][k]
    media = soma / notas
    medias.append(media)
    if media >= 15:
        print("{0:.2f}".format(media))

for i in range(len(medias)):
    medi = medias[i]
    if medi > maior:
        maior = medi
for i in range(len(medias)):
    med = medias[i]
    if med == maior:
        alunos = + 1 
        print(alunos)