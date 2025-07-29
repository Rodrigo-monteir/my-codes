import pyperclip
import keyboard
import time
from deep_translator import GoogleTranslator

while True:
    lingua = input("Digite a língua do texto para que pretende traduzir(ex: ingles, portugues):")

    linguas = ['en', 'pt', 'es', 'fr', 'de', 'it']
    linguas_1 = ['ingles', 'portugues', 'espanhol', 'frances', 'alemao', 'italiano']

    for i in range(len(linguas_1)):
        if lingua.lower() == linguas_1[i]:
            lingua = linguas[i]
            break

    texto = input("Meta o texto que pretento transformar.")

    print("Pressione Ctrl + T para iniciar o processo.")

    keyboard.wait('ctrl+t')
    time.sleep(0.5)
    print("Copiando texto...")


    print("Texto copiado")

    if not texto.strip():
        print("Nenhum texto detectado.")
        exit()

    print("tradução iniciada...")
    traduzido = GoogleTranslator(source='auto', target=lingua).translate(texto)
    print("Espere 2 segundos...")    
    time.sleep(2)

    print("Texto traduzido:", traduzido)

    pyperclip.copy(traduzido)
    print("Texto traduzido copiado para a área de transferência.")
