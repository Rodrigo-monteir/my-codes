n=int(input())
original= n
soma_cubos=0

while n >0:
    digito= n % 10
    soma_cubos= soma_cubos + digito**3
    n = n // 10

if soma_cubos == original:
    print("VERDADEIRO")
else:
    print("FALSO")
