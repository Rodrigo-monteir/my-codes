a,b,c=map(float,input().split())
x=a*a
y=b*b
z=c*c
if a>b+c:
    print("Nao se forma triangulo")
elif x==y+z:
    print("Triangulo retangulo")
elif x<y+z:
    print("Triangulo acutangulo")
elif x>y+z:
    print("Triangulo obtusangulo")
