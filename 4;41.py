l = int(input())
c = int(input())

matriz = []
media = []

for i in range(l):
    linhas = []
    linhas = list(map(int,input().split()))
    soma = sum(linhas)
    medias = int(soma / c)
    linhas.append(medias)
    media.append(medias)
    matriz.append(linhas)



for i in range(l):
    n = len(matriz[i])
    for k in range(n-1):
        print(matriz[i][k], end = " ")
    print((matriz[i][k+1]))

for i in range(l):
    med = media[i]
    if med == 20 or med >= 17:
        print("Muito Bom")
    elif med == 16 or med >= 14:
        print("Bom")
    elif med == 13 or med >= 10:
        print("Satisfaz")
    else :
        print("Sem nivel")

maior = -9999

posicoes = []

for i in range(l):
    for k in range(c):
        n = matriz[i][k-1]
        if n > maior:
            maior = n
            posicao = i,k-1
posicoes.append(posicao)

for i in range(l):
    for k in range(c):
        n = matriz[i][k-1]
        if n == maior:
            posicao = i,k-1
posicoes.append(posicao)

for i in posicoes:
    print(i[0], i[1])