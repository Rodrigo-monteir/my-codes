x=int(input())
y=int(input())
z=int(input())
if x>y and x>z:
    metros= x // 100
    centimetros= x % 100
    print(f"A altura maxima e de {metros} metro(s) e {centimetros} centimetros")

elif y>x and y>z:
    metros_y= y // 100
    centimetros_y= y % 100
    print(f"A altura maxima e de {metros_y} metro(s) e {centimetros_y} centimetros")

else :
    metros_z= z // 100
    centimetros_z= z % 100
    print(f"A altura maxima e de {metros_z} metro(s) e {centimetros_z} centimetros")
