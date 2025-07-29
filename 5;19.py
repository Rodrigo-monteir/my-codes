password = input()

bit = 0

if len(password) >= 6 and len(password) <= 12:
    bit = 1

maiuscula = False
minuscula = False
numero = False

if bit == 1:
    for i in password:
        if i.isupper():
            maiuscula = True
        elif i.islower():
            minuscula = True
        elif i.isdigit():
            numero = True

if maiuscula and minuscula and numero:
    print("VALIDA")
else:
    print("INVALIDA")