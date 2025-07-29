n = int(input())

maior_soma = -9999

for i in range(n):
    numero = int(input())
    soma = 0
    for k in str(numero):
        soma += int(k)
    if soma > maior_soma:
        maior_soma = soma
        maior_numero = numero

numero_ordenado = ''.join(sorted(str(maior_numero)))

print(numero_ordenado)