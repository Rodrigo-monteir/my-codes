from math import inf
n= int(input())

vector= []
resultados= []

maior= -inf
menor= inf
resultado_m= -inf

resultado= 0
resultado_1= 0
resultado_2= 0
resultado_3= 0

for i in range(n):
    valor= (int(input()))
    vector.append(valor)
    if valor > maior:
        maior= valor
    if valor < menor:
        menor= valor

diferenca= maior - menor
print(diferenca)

for i in range(n):
    if vector[i] == 20 and vector[i] >= 16:
        resultado += 1
    elif vector[i] <= 15 and vector[i] >= 11:
        resultado_1 += 1
    elif vector[i] <= 10 and vector[i] >= 6:
        resultado_2 += 1
    elif vector[i] <= 5 and vector[i] >= 1:
        resultado_3 += 1

resultados.append(resultado)
resultados.append(resultado_1)
resultados.append(resultado_2)
resultados.append(resultado_3)

print("[1,5]=",resultado_3,sep="")
print("[6,10]=",resultado_2,sep="")
print("[11,15]=",resultado_1,sep="")
print("[16,20]=",resultado,sep="")

for i in range(len(resultados)):
    if resultados[i] > resultado_m:
        resultado_m = resultados[i]

if resultado_m == resultado:
    print("[16,20]")
elif resultado_m == resultado_1:
    print("[11,15]")
elif resultado_m == resultado_2:
    print("[6,10]")
elif resultado_m == resultado_3:
    print("[1,5]")
