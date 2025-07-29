import math
x,y=map(int,input().split())
v=math.pi*(x**2)*y
ab=math.pi*(x**2)
al=2*math.pi*x*y
at=(2*ab)+al
print("O volume e: {0:.2f}".format(v))
print("A area da base e: {0:.2f}".format(ab))
print("A area lateral e: {0:.2f}".format(al))
print("A area total e: {0:.2f}".format(at))
