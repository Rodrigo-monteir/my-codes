cfixo= float(input())
cbase= float(input())
cextra= float(input())
d= int(input())
n= int(input())

PI= 3.14

raio= d / 2
area= PI * raio**2

custo= cfixo + (cbase * area) + (n * cextra * area)

preco= 1.5 * custo

print("{0:.2f}".format(preco))