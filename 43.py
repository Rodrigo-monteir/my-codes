n = int(input())

maior = -9999
menor = 9999

posicao_m = 0
posicao_min = 0

for i in range(n):
    num = int(input())
    if num % 2 != 0:
        if num > maior:
            maior = num
            posicao_m = i + 1
        if num < menor:
            menor = num
            posicao_min = i + 1

print(menor)
print(posicao_min)
print(maior)
print(posicao_m)