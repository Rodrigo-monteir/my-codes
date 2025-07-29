texto = input()

novo =  ""

for i in range(len(texto)):
    if texto[i] not in " aeiouAEIOU":
        novo += texto[i]
print(novo)
