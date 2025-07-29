n=int(input())
maxn=-9999
for i in range(1,n+1):
    valor=int(input())
    if valor>=1 and valor<=100:
        valor=valor
    if valor>maxn:
        maxn=valor
    
print("O maior e o",maxn,"e esta na posicao",i)
