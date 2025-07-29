texto = input()

vogal_1 = 0
vogal_2 = 0
vogal_3 = 0
vogal_4 = 0
vogal_5 = 0

for i in range(len(texto)):
    if texto[i] == "a" or texto[i] == "A":
        vogal_1 += 1
    elif texto[i] == "e" or texto[i] == "E":
        vogal_2 += 1
    elif texto[i] == "i" or texto[i] == "I":
        vogal_3 += 1
    elif texto[i] == "o" or texto[i] == "O":
        vogal_4 += 1
    elif texto[i] == "u" or texto[i] == "U":
        vogal_5 += 1

print(vogal_1,vogal_2,vogal_3,vogal_4,vogal_5)