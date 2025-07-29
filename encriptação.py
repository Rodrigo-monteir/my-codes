from cryptography.fernet import Fernet

opção = input("Escolha uma opção (1 - Criptografar, 2 - Descriptografar): ")

if opção not in ['1', '2']:
    print("Opção inválida. Encerrando o programa.")
    exit()

if opção == '1':
    chave = Fernet.generate_key()
    print("Chave gerada:", chave.decode())
    fernet = Fernet(chave)

    mensagem = input("Digite a mensagem a ser criptografada: ")
    mensagem_criptografada = fernet.encrypt(mensagem.encode())
    print("Mensagem criptografada:", mensagem_criptografada.decode())

elif opção == '2':
    chave = input("Digite a chave de acesso para descriptografar a mensagem: ").encode()
    mensagem_criptografada = input("Digite a mensagem criptografada: ")
    try:
        mensagem_descriptografada = fernet.decrypt(mensagem_criptografada.encode())
        print("Mensagem descriptografada:", mensagem_descriptografada.decode())
    except Exception as e:
        print("Erro ao descriptografar. Verifique a chave e a mensagem.")