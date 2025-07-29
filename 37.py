n = int(input())

soma_alturas = 0
maior_altura = -9999

for i in range(n):
    nome = input()
    altura = int(input())
    soma_alturas += altura
    media = soma_alturas / n
    if altura > maior_altura:
        maior_altura = altura
        maior_nome = nome
print("SOMA:",soma_alturas)
print("MEDIA: {0:.2f}".format(media))
print("ALTURA MAX:",maior_altura)
print("PESSOA MAIS ALTA:",maior_nome)