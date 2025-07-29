X,Y = map(float, input().split())

comprimento= Y / X

perimetro= 2 * (X + comprimento)

lado_quadrado= perimetro / 4

print("{:.2f}".format(lado_quadrado))
