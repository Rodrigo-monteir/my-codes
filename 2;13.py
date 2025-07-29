x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

det = x*b - a*y

if det == 0:
    det1 = y*c - b*z
    det2 = x*c - a*z

    if det1 == 0 and det2 == 0:
        print("Indeterminado")
    else:
        print("Impossivel")
else:
    f = (z*b - y*c) / det
    f2 = (x*c - z*a) / det
    print("{0:.2f} {1:.2f}".format(f, f2))
