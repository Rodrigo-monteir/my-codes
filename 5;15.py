texto = input()

for i in  range(65,91):
    if chr(i) in texto:
        print(chr(i),"-",texto.count(chr(i))) 