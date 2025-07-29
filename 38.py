n = int(input())

while n >= 10:
    soma = 0
    for i in str(n):
        soma += int(i)
    n = soma
print(n)
