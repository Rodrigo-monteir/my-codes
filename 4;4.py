import math
n=(int(input()))

nomes= []
notas= []

for i in range(n):
    nomes.append(input())
    notas.append(int(input()))

nota_max=-math.inf

for i in range(n):
    if notas[i] > nota_max:
        nota_max = notas[i]
for i in range(n):
    if notas[i] == nota_max:
        print("Melhor nota foi",nota_max,"do(a)",nomes[i])
