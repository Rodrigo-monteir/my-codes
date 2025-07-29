n= int(input())

vector_1= []
vector_2= []
vectort= []

for i in range(n):
    vector_1.append(int(input()))
for i in range(n):
    vector_2.append(int(input()))
for i in range(n):
    vectort.append(vector_1[i])
    vectort.append(vector_2[i])
for i in vectort:
    print(i)