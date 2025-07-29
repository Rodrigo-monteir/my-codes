x=float(input())
y=float(input())
z=float(input())

a=x+y
b=y+z
c=z+x

if a > b and a > c:
    print("{0:.0f}".format(a))
elif b > a and b > c:
    print("{0:.0f}".format(b))
else :
    print("{0:.0f}".format(c))
