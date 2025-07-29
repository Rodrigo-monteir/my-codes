und=int(input())
preco=float(input())
cor=input()

precot=und * preco
d = 0

if und > 5:
    d = 10
elif cor == "VERMELHO":
    d = 5

d_euro= precot * (d/100)
a_pagar= precot - d_euro

print("A PAGAR: {0:.2f}".format(a_pagar))
print("DESCONTO: {0:.2f}".format(d_euro))
