x = float(input())
y = float(input())

imc = y / (x**2)

print("{0:.2f}".format(imc))

if imc <= 18.5:
    print("Abaixo peso ideal")
elif 18.5 < imc <= 24.9:
    print("Peso ideal")
elif 25.0 <= imc <= 29.9:
    print("Sobrepeso")
elif 30.0 <= imc <= 34.9:
    print("Obesidade grau I")
elif 35.0 <= imc <= 39.9:
    print("Obesidade grau II")
elif imc >= 40.0:
    print("Obesidade grau III")
