texto=input()

texto_invert=[]

for i in range(len(texto)):
    texto_invert.insert(0,texto[i])

for i in range(len(texto_invert)):
    print(texto_invert[i],end="")