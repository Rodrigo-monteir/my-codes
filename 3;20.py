num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 <= num2 <= num3:
    ordem = (num1, num2, num3)
elif num1 <= num3 <= num2:
    ordem = (num1, num3, num2)
elif num2 <= num1 <= num3:
    ordem = (num2, num1, num3)
elif num2 <= num3 <= num1:
    ordem = (num2, num3, num1)
elif num3 <= num1 <= num2:
    ordem = (num3, num1, num2)
else:
    ordem = (num3, num2, num1)

for numero in ordem:
    print(numero)
