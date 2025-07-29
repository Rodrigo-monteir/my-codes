n= int(input())

vector_a= []
vector_b= []
vector_c= []
vector_d= []

for i in range(n):
    vector_a.append(int(input()))
for i in range(n):
    vector_b.append(int(input()))
for i in range(n):
    vector_c.append(vector_a[i] + vector_b[i])

for i in vector_c:
    print(i)

for a in vector_a:
    if a not in vector_b:
        vector_d.append(a)
for b in vector_b:
    if b not in vector_a:
        vector_d.append(b)

for i in vector_d:
    print(i)