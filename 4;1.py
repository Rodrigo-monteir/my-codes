lista=[]
n=(int(input()))

for i in range(n):
    lista.append(int(input()))
soma=0
produto=1

for i in lista:
    soma += i
    produto *= i
print(soma)
print(produto)
