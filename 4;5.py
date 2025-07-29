import math
n=(int(input()))

notas= []
notas_max= []

media_0=0
nota_max= -math.inf

for i in range(n):
    notas.append(float(input()))
    media_0 += notas[i]
media = media_0 / n
print("MEDIA:",media)
print("NOTA SUPERIOR A MEDIA:")
for i in range(n):
    if notas[i] > media:
        print(i + 1)
print("MELHORES NOTAS:")
for i in range(n):
    if notas[i] > nota_max:
        nota_max = notas[i]
for i in range(n):
    if notas[i] == nota_max:
        print(i + 1)
