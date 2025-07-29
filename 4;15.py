n= int(input())

vector= []

produto= 1

for i in range(n):
    valor= int(input())
    vector.append(valor)
    produto *= valor
print(produto)
for i in range(1):
    if vector[0] >= vector[1]:
        posicao= i + 1
        print(vector[0]," (",posicao,")",sep="")
for i in range(1, n - 1):
    if vector[i] >= vector[i - 1] and vector[i] >= vector[i + 1]:
        posicao = i + 1
        print(vector[i], " (", posicao, ")", sep="")
for i in range(1):
    if vector[-1] >= vector[i - 1]:
        posicao= n
        print(vector[-1]," (",posicao,")",sep="")