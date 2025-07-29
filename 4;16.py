n= int(input())

vector= []

contador= 0

for i in range(n):
    vector.append(int(input()))

ler= int(input())
num_ler= vector.count(ler)

if num_ler > 0:
    print(num_ler)
else:
    print("NAO ENCONTRADO")

for i in range(1, n - 1):
    if vector[i] >= vector[i - 1] and vector[i] >= vector[i + 1]:
        contador += 1

if contador >= n - 2:
    print("ORDENADO")
else:
    print("NAO ORDENADO")
