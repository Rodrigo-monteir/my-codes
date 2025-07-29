x=int(input())
y=int(input())

pt = x * y
d = 0

if pt >= 200:
    d = 20
elif pt >= 100:
    d = 10

desconto_euros = pt * (d / 100)
a_pagar = pt - desconto_euros

print("TOTAL: {0:.2f}".format(pt))
print("TAXA DESCONTO: {0}%".format(d))
print("MONTANTE DESCONTO: {0:.2f}".format(desconto_euros))
print("A PAGAR: {0:.2f}".format(a_pagar))
