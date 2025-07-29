import math
n=(int(input()))

maior= -math.inf
menor= -math.inf
nomem= " "
nomen= " "

for i in range(n):
    nome=input()
    nota=(float(input()))
    if nota <= 20:
        if nota > maior:
            menor= maior
            nomen= nomem
            maior= nota
            nomem= nome
        elif nota > menor:
            menor= nota
            nomen= nome
print(nomem)
print("{0:.0f}".format(maior))
print(nomen)
print("{0:.0f}".format(menor))
