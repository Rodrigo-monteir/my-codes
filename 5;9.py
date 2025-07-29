n = int(input())

text = []

for _ in range(n):
    texto = input().split()
    text.extend(texto)

for i in range(len(text)):
    if i % 2 == 0:
        text[i] = text[i].upper()

print(' '.join(text))

