def cifrarCesar(texto, chave):
    cifra = ""
    for char in texto:
        if 'A' <= char <= 'Z':
            cifra += chr(((ord(char) - ord('A') + chave) % 26) + ord('A'))
        elif 'a' <= char <= 'z':
            cifra += chr(((ord(char) - ord('a') + chave) % 26) + ord('a'))
        else:
            cifra += char
    return cifra

def decifrarCesar(texto, chave):
    return cifrarCesar(texto, -chave)

mensagem_original = "Olá Mundo!" #pode ser inserida qualquer palavra/frase
deslocamento = 2 #de -26 até 26

mensagem_cifrada = cifrarCesar(mensagem_original, deslocamento)
mensagem_decifrada = decifrarCesar(mensagem_cifrada, deslocamento)

print("Cifrada:", mensagem_cifrada)
print("Decifrada:", mensagem_decifrada)
