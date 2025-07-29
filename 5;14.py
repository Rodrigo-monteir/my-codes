texto = input().split()

maior = -9999
pal = ""

for i in range(len(texto)):
    if len(texto[i]) > maior:
        maior = len(texto[i])
        pal = texto[i]
print(pal)