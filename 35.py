n= int(input())

vector= []

for i in range(n):
    vector.append(int(input()))

for i in range(1, n - 1):
    if vector[i] > vector[i - 1] and vector[i] >= vector[i + 1]:
        print(vector[i],end=" ")