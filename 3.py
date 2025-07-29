x=int(input())
y=int(input())
z=int(input())

maior=-9999
menor=9999
maior2=0

if x > maior:
    maior= x
elif x < menor:
    menor= x
elif y > x:
    maior= y
elif y < x:
    menor= y
elif z > y:
    maior= z
elif z < y:
    menor= z
if x < maior and x > menor:
    maior2= x
elif y < maior and y > menor:
    maior2= y
else:
    maior2= z

print(menor)
print(maior2)
print(maior,)
