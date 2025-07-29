texto = input()

novo =  ""

for i in range(len(texto)):
    if texto[i] == "a":
        novo += "A"
    elif texto[i] == "e":
        novo += "E"
    elif texto[i] == "i":
        novo += "I"
    elif texto[i] == "o":
        novo += "O"
    elif texto[i] == "u":
        novo += "u"
    else :
        novo += texto[i]

print(novo)
