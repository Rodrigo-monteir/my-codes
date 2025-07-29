import calendar

ano=int(input())

sextas_13=0

if ano >= 1998:
    ver= ano / 4
    ver_2= ano / 100
    ver_3= ano / 400

    for i in range(1, 13):
        if calendar.weekday(ano, i, 13) == 4:
            sextas_13 +=1
    print(sextas_13)
else:
    print("Ano Invalido")
