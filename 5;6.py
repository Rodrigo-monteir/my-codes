texto = input()

maiusculas = 0
minusculas = 0

for letra in texto:
    if letra.islower():
        minusculas += 1
    elif letra.isupper():
        maiusculas += 1

print("MAIUSCULAS:",maiusculas)
print("MINUSCULAS:",minusculas)
