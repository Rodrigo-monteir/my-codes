n = int(input())

binario =  []
expoentes = []

expoente = 1
expoentes.append(expoente)
for i in range(n):
    binario.append(int(input()))
    expoente *= 2
    expoentes.append(expoente)
expoentes.pop()
expoentes.reverse()

soma = 0

for i in range(n):
    num = binario[i]
    expo = expoentes[i]
    if num == 1:
        soma += expo
print(soma)