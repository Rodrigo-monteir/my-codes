a,b,c = map(int,input().split())

maior = -9999
menor = 9999
iter = 0

if a > maior:
    maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
if a < menor:
    menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

maior_qua = maior ** 2
quadrado_1 = menor ** 2
if a < maior and a > menor:
    iter = a
if b < maior and b > menor:
    iter = b
if c < maior and c > menor:
    iter = c
quadrado_2 = iter ** 2

soma_qua= quadrado_1 + quadrado_2

if soma_qua == maior_qua:
    print("E PITAGORICO (NAO E PITAGORICO)")
else :
    print("NAO E PITAGORICO")