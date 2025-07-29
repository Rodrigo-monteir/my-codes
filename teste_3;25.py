n=int(input())
maiors=-9999
menors=9999
nomes=" "
nomem=" "
premio=0
salariot=0
premio5=0
msalario=0

for i in range(n):
    nome=input()
    salario=float(input())
    if salario >= 1000:
        premio= 5/100
        premio5=premio5+1
    elif salario >= 800:
        premio= 8/100
    elif salario >= 500:
        premio= 10/100
    salariot= salario +(premio*salario)
    if salariot > maiors:
        maiors= salariot
        nomem=nome
    elif salariot < menors:
        menors= salariot
        nomes= nome
print("{0:.2f}".format(maiors))
print("{0:.2f}".format(menors))
print(nomem)
print(premio5)
msalario= (maiors + menors)/n
print("{0:.2f}".format(msalario))
    
