import math
a,b,c=map(float,input().split())
f=(-b+math.sqrt(b**2 - 4*a*c))/(2*a)
v=(-b-math.sqrt(b**2 - 4*a*c))/(2*a)
print("{0:.2f} {1:.2f}".format(v,f))
