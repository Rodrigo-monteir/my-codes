n= int(input())

if n == 1 or n == 0:
    print('0')

elif n == 2 or n == 3:
    print('1')

elif n % 2 != 0 and n % 3 != 0:
    print('1')

else:
    print('0')