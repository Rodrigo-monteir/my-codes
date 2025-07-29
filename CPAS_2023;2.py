o,p,ai,d = map(int,input().split())

for i in range(16):
    if o == p:
        print("N")
        break
    if ai == p:
        print("N")
        break

    if d == -1:
        ai = ai + 1
        if ai > 15:
            ai = 0
        if ai == p:
            print("N")
            break
        elif ai == o:
            print("S")
            break

    elif d == 1:
        ai = ai - 1
        if ai < 0:
            ai = 15
        if ai == p:
            print("N")
            break
        elif ai == o:
            print("S")
            break