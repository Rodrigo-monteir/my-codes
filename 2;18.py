x,y,z=map(int,input().split())
a,b,c=map(int,input().split())

det= x * b - a * y
if det == 0:
    det1= y * b - c * y
    det2= x * c - a * z

    if det1 == 0:
        print("Indeterminado")
    elif det2 == 0:
        print("Indeterminado")
    else :
        print("Impossivel")
else :
    f=(z*x - y*c) / (x*b - y*a)
    f2=(x*c - z*a) / (x*b - y*a)
    print("{0:.2f} {1:.2f}".format(f,f2))
