import math
n=(int(input()))

sexo_f= [ ]
sexo_m= [ ]
altura_f= [ ]
altura_m= [ ]

maior= -math.inf
menor= math.inf
maiorm= -math.inf
menorm= math.inf

media_f= 0
media_m= 0

for i in range(n):
    sexo=input()
    altura=(float(input()))
    if sexo == "F":
        sexo_f.append(sexo)
        altura_f.append(altura)
    elif sexo == "M":
        sexo_m.append(sexo)
        altura_m.append(altura)

cont_f= len(altura_f)
cont_m= len(altura_m)

for i in range(cont_f):
    media_f += altura_f[i]
    if altura_f[i] > maior:
        maior= altura_f[i]
    if altura_f[i] < menor:
        menor= altura_f[i]

for i in range(cont_m):
    media_m += altura_m[i]
    if altura_m[i] > maiorm:
        maiorm= altura_m[i]
    if altura_m[i] < menorm:
        menorm= altura_m[i]

if cont_f > 0:
    media_ft= media_f / cont_f
    print("MEDIA MULHERES: {0:.0f}".format(media_ft))

if cont_m > 0:
    media_mt= media_m / cont_m
    print("MEDIA HOMENS: {0:.0f}".format(media_mt))

if cont_f == cont_m:
    print("MAIS BAIXA: {0:.0f}".format(menor))
    print("MAIS ALTA: {0:.0f}".format(maior))
    print("MAIS BAIXO: {0:.0f}".format(menorm))
    print("MAIS ALTO: {0:.0f}".format(maiorm))

elif cont_f > cont_m:
    print("MAIS BAIXA: {0:.0f}".format(menor))
    print("MAIS ALTA: {0:.0f}".format(maior))

else :
    print("MAIS BAIXO: {0:.0f}".format(menorm))
    print("MAIS ALTO: {0:.0f}".format(maiorm))

