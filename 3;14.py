n = int(input())
divisores = 0
divisores_n = []

for i in range(1, n + 1):
    divisores= n % i
    if  divisores== 0:         
        divisores_n.append(i)

for divisor in divisores_n:
    print(divisor)
