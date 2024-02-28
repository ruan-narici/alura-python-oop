import random


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")


def carregar_palavra_secreta():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for palavra in arquivo:
            palavras.append(palavra.strip().lower())
    palavra = palavras[random.randrange(0, len(palavras))]
    return palavra


def carregar_letras_acertadas(palavra_secreta: str):
    return ["_" for palavra in palavra_secreta]


def exibe_palavras_acertadas(letras_corretas :list):
    print("Tente adivinhar a palavra: ")
    print(letras_corretas)


def exibe_chances_restantes(chances :int):
    desenha_forca(chances)
    print("chances: {0}".capitalize().format(chances))


def perguntar_chute():
    return input("digite uma letra: ".capitalize()).lower().strip()


def verifica_acerto(chute :str, palavra :str, index_palavra :int, letras_corretas :list):
        for letra in palavra:
            if chute == letra:
                letras_corretas[index_palavra] = letra
            index_palavra += 1


def imprime_mensagem_final(acertou, enforcou, palavra_secreta):
    if acertou:
        imprime_mensagem_vencedor()
    elif (enforcou):
        imprime_mensagem_perdedor(palavra_secreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def jogar():
    imprime_mensagem_abertura()
    palavra = carregar_palavra_secreta()
    letras_corretas = carregar_letras_acertadas(palavra)

    enforcou = False
    acertou = False
    chances = 7

    exibe_palavras_acertadas(letras_corretas)

    while not enforcou and not acertou:
        index_palavra = 0
        chute = perguntar_chute()
        if chute in palavra:
            verifica_acerto(chute, palavra, index_palavra, letras_corretas)
        else:
            chances -= 1
            exibe_chances_restantes(chances)
        exibe_palavras_acertadas(letras_corretas)

        acertou = "_" not in letras_corretas
        enforcou = chances == 0

        imprime_mensagem_final(acertou, enforcou, palavra)

if __name__ == "__main__":
    jogar()