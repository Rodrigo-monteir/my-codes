n,x = map(int,input().split())

nomes = []
notas = []

for i in range(x):
    nome = input()
    nota = []
    nota = list(map(int,input().split()))
    soma = sum(nota)
    media = soma / n
    nomes.append(nome)
    notas.append(media)

for i in range(x):
    if notas[i] >= 10:
        print(nomes[i],">Aprovado(a)",sep="")