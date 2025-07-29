import math

n=(int(input()))

idade= [ ]
idade1= [ ]
idades= [ ]
filhos= [ ]
rendi= [ ]

media= 0
rendi_min= 0
filhos_max= -math.inf

for i in range(n):
    idade2, idade4=map(int,input().split())
    idade.append(idade2)
    idade1.append(idade4)
    filhos.append(int(input()))
    rendi.append(float(input()))
    if filhos[i] > filhos_max:
        filhos_max = filhos[i]
    if rendi[i] < 20000:
        rendi_min +=1

idades= idade + idade1
rendi_min= (rendi_min / n) * 100

N= len(idades)

for i in range(N):
    media += idades[i]
print("IDADE MEDIA PROGENITORES: {0:.2f}".format(media / N))
print("NUMERO MAXIMO DE FILHOS POR FAMILIA:",filhos_max)
print("PERCENTAGEM DE FAMILIAS COM RENDIMENTO INFERIOR A 20000: {0:.2f}".format(rendi_min),"%",sep="")
