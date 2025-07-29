import math
n= int(input())

vector= []

maior= -math.inf
menor= math.inf

contador=0

if n >= 2:
    for i in range(n):
        valor= int(input())
        vector.append(valor)
    prim= vector[0]
    ult= vector[-1]
    soma= prim + ult
    for i in range(n):
        if vector[i] >= soma:
            posicao= i + 1
            contador += 1
            print(vector[i]," (",posicao,")",sep="")
    print(contador)
    
    list.reverse(vector)

    for i in vector:
        print(i)