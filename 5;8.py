texto = input()

novo = ""

for i in texto:
    if i not in novo:
        novo += i
print(novo)