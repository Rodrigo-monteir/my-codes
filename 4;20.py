n= int(input())

vector= []
vector_t= []

for i in range(n):
    vector.append(int(input()))
for i in range(n):
    vector_t.append(vector[i]*vector[i])
for i in vector_t:
    print(i)