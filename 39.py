n,k = map(int,input().split())

fumados = n
beatas = k

beatas_atual = fumados

cigarros = beatas_atual / 3
cigarro_atual = cigarros / 3

cigarros_total = fumados + cigarros + cigarro_atual

print("{0:.0f}".format(cigarros_total))