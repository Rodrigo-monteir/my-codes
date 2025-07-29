import math
n=int(input())

vector= []

maior= -math.inf
menor= math.inf

for i in range(n):
    valor=int(input())
    vector.append(valor)
    if valor> maior:
        maior= valor
        posicao_maior= i + 1
    elif valor < menor:
        menor= valor
        posicao_menor= i + 1
print(maior," (",posicao_maior,")",sep="")
print(menor," (",posicao_menor,")",sep="")

tamanho= len(vector)

if tamanho % 2 == 0:
    indice1= n // 2 - 1
    indice2= n // 2
    elem1 = vector[indice1]
    elem2 = vector[indice2]
    if elem1 % 2 == 0 and elem2 % 2 == 0:
        resultado = "PAR"
    elif elem1 % 2 != 0 and elem2 % 2 != 0:
        resultado = "IMPAR"
else:
    indice = n // 2
    elem = vector[indice]
    resultado = "PAR" if elem % 2 == 0 else "IMPAR"

print(resultado)

acumulado= 0

for i in range(n):
    if vector[i] >= elem:
        posicao= i + 1
        acumulado +=1
        print(vector[i]," (",posicao,")",sep="")
print(acumulado)