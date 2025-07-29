x=float(input())
y=float(input())
op=input()
if op=="+":
    print("{0:.2f}".format(x+y))
elif op=="-":
    print("{0:.2f}".format(x-y))
elif op=="*":
    print("{0:.2f}".format(x*y))
elif op=="/":
    print("{0:.2f}".format(x/y))
