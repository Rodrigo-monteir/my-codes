texto = input()
texto_1 = texto.split()

novo = ""

for i in texto_1:
    if i.isalpha():
        novo += i + " "

novo = " ".join(novo.split())

print(novo)