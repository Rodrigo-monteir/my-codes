import math
x,y,z=map(int,input().split())
s=(x+y+z)/2
a=math.sqrt(s*(s-x)*(s-y)*(s-z))
print("{0:.2f}".format(a))
