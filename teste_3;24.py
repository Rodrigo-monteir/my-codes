n=int(input())
apoio=0
maiorn=-9999
idadem=0
mediai=0
mediai1=0
positiva=0
notap=0
for i in range(n):
    nome=input()
    idade=int(input())
    nota=float(input())
    if nota <= 9:
        apoio=apoio+1
    if nota > maiorn:
        maiorn= nota
        idadem= idade
    mediai= (idade+mediai)
    mediai1=mediai/n
    if nota > 9:
        positiva=positiva+1
notap= (positiva/n)*100
print(apoio)
print(idadem)
print("{0:.2f}".format(mediai1))
print("{0:.0f}".format(notap),"%")
