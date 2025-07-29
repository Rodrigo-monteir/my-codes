n=(int(input()))

vetor= []
neg= 0
pos= 1

for i in range(n):
    vetor.append(int(input()))
for i in range(n):
    if vetor[i] < 0:
        vetor[i] = neg
        vetor.append(vetor[i])
    else :
        vetor[i] = pos
        vetor.append(vetor[i])
for i in range(n):
    print(vetor[i])
            
