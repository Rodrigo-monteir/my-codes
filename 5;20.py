n = int(input())

textos = []

for i in range(n):
    texto = input()
    textos.append(texto)

x, y = map(int, input().split())

if x > n:
    exit()

matriz = []

for i in range(x):
    linha = list(map(int, input().split()))
    matriz.append(linha)

for i in range(x):
    novo = ""
    for k in range(y):
        num = matriz[i][k]
        novo += textos[i][num]
    print(novo)