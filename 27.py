import math

x,y= map(float, input().split())

comprimento= 5.5

lado_metros= y / 100

perimetro= 2 * (x + comprimento)
area_quarto = x * comprimento
area_placa = lado_metros ** 2
num_placas = math.ceil(area_quarto / area_placa)
custo_total = num_placas * 5

print("{0:.2f}".format(perimetro))
print("{0:.2f}".format(area_quarto))
print("{0:.2f}".format(area_placa))
print("{0:.2f}".format(num_placas))
print("{0:.2f}".format(custo_total))
