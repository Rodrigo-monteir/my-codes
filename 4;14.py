import math
n= int(input())

vector= []

maior= -math.inf
soma=0

for i in range(n):
    valor= int(input())
    vector.append(valor)
    soma += valor
media= soma / n

print(soma)
print("{0:.2f}".format(media))
for i in range(n):
    if abs(vector[i]-media)<= 1:
        print(i + 1)
    if vector[i] == maior:
        print(i + 1)