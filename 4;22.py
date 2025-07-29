x=int(input())
y=int(input())

vector= []

expoente= x
vector.append(expoente)

for i in range(1, y):
    expoente *= x
    expoente = expoente  
    
    vector.append(expoente)
for i in vector:
    print(i)