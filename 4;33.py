p = int(input())
q = int(input())

matriz = []

for i in range(p):
    linha = []
    linha = list(map(int,input().split()))
    matriz.append(linha)

soma = 0

for i in range(p):
    for k in range(q-1):
        n = matriz [i] [k+1]
        if n >= 10:
            soma += n
        print(matriz [i][k], end= " ")
    print(matriz[i][k+1])
print(soma)