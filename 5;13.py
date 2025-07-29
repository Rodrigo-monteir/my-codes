texto = input()

s = 0

for i in range(len(texto)):
    if texto[i] >= "A" and texto[i] <= "Z" or texto[i] >= "a" and texto[i] <= "z":
        s += 1
print(s)