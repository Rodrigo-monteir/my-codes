texto = input()
novo = texto.split()

grupo = ""

for i in novo:
    contador = 0
    letra = i
    for i in range(len(novo)):
        if letra not in grupo:
            grupo += letra
            contador= novo.count(letra)
            print(contador)