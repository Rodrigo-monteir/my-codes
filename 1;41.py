decimal = int(input())

if decimal == 0:
    print(0)
else:
    binario = ""
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2

    print(binario)