x= float(input())

troco= 100 - x

valores= [100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

for valor in valores:
    quantidade= int(troco // valor)
    troco -= quantidade * valor
    print(f"{quantidade}x{valor}")