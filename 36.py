n = int(input())

lista = []

for i in range(n):
    lista.append(int(input()))

maior_comprimento = 0
algarismo_maior = 0
comprimento_atual = 1
algarismo_atual = lista[0]

for i in range(n):
    if lista[i] == algarismo_atual:
        comprimento_atual += 1
    else:
        if comprimento_atual > maior_comprimento:
            maior_comprimento = comprimento_atual
            algarismo_maior = algarismo_atual
        
        algarismo_atual = lista[i]
        comprimento_atual = 1

if comprimento_atual > maior_comprimento:
    maior_comprimento = comprimento_atual
    algarismo_maior = algarismo_atual

print(maior_comprimento)
print(algarismo_maior)
