import pyperclip
import keyboard
import time
from deep_translator import GoogleTranslator

print("Pressione Ctrl + C para copiar texto.")
print("Pressione Ctrl + T para traduzir o texto copiado.")

keyboard.wait('ctrl+t')
time.sleep(0.5)
print("Copiando texto...")
texto = pyperclip.paste()
print("Texto copiado:")
if not texto.strip():
    print("Nenhum texto copiado.")
    exit()
print("tradução iniciada...")
traduzido = GoogleTranslator(source='auto', target='pt').translate(texto)
print("Espere 2 segundos...")    
time.sleep(2)
print("Texto traduzido:", traduzido)
pyperclip.copy(traduzido)
print("Texto traduzido copiado para a área de transferência.")