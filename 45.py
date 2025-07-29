import random

vidas = 3
contador = 0
while vidas > 0:
    numero = random.randint(1, 3)
    num = int(input("Digite um número de 1 a 3? "))

    if num == numero:
        contador += 1
        print("ACERTOU")
        print("Nº VIDAS:",vidas)
        print("CONTADOR:",contador)
    else :
        vidas -= 1
        contador -= 1
        print("ERROU")
        print("Nº VIDAS:",vidas)
        print("CONTADOR:",contador)