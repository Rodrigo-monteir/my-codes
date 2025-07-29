idade= []
adulto= []
crianca= []

pesot= 0

n=(int(input()))

while n != 0:
    idade.append(n)
    if n >=18:
        peso= 75
        adulto.append(n)
    else :
        peso= 45
        crianca.append(n)
    pesot += peso
    n=(int(input()))
print("No aviao viajam",len(adulto),"adulto(s) e",len(crianca),"nao adulto(s)")
print("O peso estimado e de",pesot,"kg")

