n= int(input())

idades= []
alturas= []

soma= 0
maiores= 0

for i in range(n):
    idades.append(int(input()))
    alturas.append(int(input()))

for i in range(n):
    soma += alturas[i]
media= soma / n

for i in range(n):
    if alturas[i] > media:
        if idades[i] > 15:
            maiores += 1
print(maiores)