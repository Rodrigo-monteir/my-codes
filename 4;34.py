p = int(input())
q = int(input())

matriz = []

for i in range(p):
    linha = []
    linha = list(map(int,input().split()))
    matriz.append(linha)

for i in range(p):
    soma_linha = sum(matriz[i])
    print("A soma da linha",i+1,"e", soma_linha)

for i in range(q):
    soma_colunas = 0
    for k in range(p):
        soma_colunas += matriz[k][i]
    print("A soma da coluna",i+1,"e",soma_colunas)