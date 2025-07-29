n=int(input())
primo= 0
multiplos_3= []
for i in range(n):
    numero=int(input())
    primo = numero % 3
    if  primo == 0:
        multiplos_3.append(numero)
for multiplo in multiplos_3:
    print(multiplo)
