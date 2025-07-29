n=int(input())
soma=0

for i in range(n):
    valor=int(input())
    soma=soma+valor
print("{:.2f}".format(soma/n))
