import math
n=int(input())

num= [ ]
impar= [ ]
posicao= [ ]

menor= math.inf

for i in range(n):
    valor=int(input())
    num.append(valor)
    if valor < menor:
        menor= valor
        posicao_menor= i + 1
print(menor, " (", posicao_menor, ")", sep="")

prim= num[0]
ultm= num[-1]

somaf= prim + ultm

fatorial= 1

for i in range(1, somaf + 1):
    fatorial *= i
print(fatorial)

for i in range(n):
    if num[i] % 2 != 0:
        impar.append(num[i])  
        posicao.append(i + 1)  

imparn= len(impar)
for i in range(imparn):
    print(impar[i], " (", posicao[i], ")", sep="")
print(imparn)
