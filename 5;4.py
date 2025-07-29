texto = input()

outro = texto.split()
ultimo = outro[-1]

termo = ["de","da","e","dos","das","do"]

novo = ''

for i in range(1,len(outro)-1):
    if outro[i] not in termo:
        novo += " "+outro[i][0]+"."
print(ultimo,", ",outro[0]+novo,sep = "")