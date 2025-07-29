n= int(input())
fatorial= 1
inteiro= 0

for i in range(n):
    fa= float(input())
    inteiro= fa % 1
    if inteiro == 0:
        fa= int(fa)
        fatorial= 1
        for i in range(1, fa + 1):
            fatorial *= i
        print(fatorial)
    else:
        erro= inteiro
