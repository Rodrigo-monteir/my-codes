soma_correta= 134 + 78
tentativas= 3
acertou= False

while tentativas > 0:
    resposta=(int(input()))
    if resposta == soma_correta:
        print("Acertou")
        acertou= True
        break
    else:
        tentativas -= 1

if not acertou:
    print("Falhou")
