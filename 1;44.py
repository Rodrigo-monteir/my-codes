funcao = input()

if funcao == "AND":
    a,b = map(int,input().split())
    cont = a * b
elif funcao == "NOT":
    a = int(input())
    if a == 1:
        cont = 0
    elif a == 0:
        cont = 1
elif funcao == "OR":
    a,b = map(int,input().split())
    cont = a + b

print(cont)