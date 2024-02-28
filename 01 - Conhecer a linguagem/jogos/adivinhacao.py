import random


def imprime_inicio_jogo():
    print("*********************************")
    print("Bem vindo ao jogo da adivinhacao!")
    print("*********************************")


def receber_nivel_dificuldade():
    print("(1) FACIL, (2) MEDIO, (3) DIFICIL")
    return int(input("Defina o nivel: "))


def definir_numero_tentativas(dificuldade_nivel :int):
    if (dificuldade_nivel == 1):
        return 20
    elif (dificuldade_nivel == 2):
        return 10
    else:
        return 5


def imprime_tentativas_restantes(rodada :int, total_tentativas :int):
    print("Tentativa {} de {}".format(rodada, total_tentativas))


def receber_numero_chutado():
    chute = int(input("Digite um numero entre 1 e 100: "))
    print("Voce digitou o numero: ", chute)
    return chute


def jogar():
    imprime_inicio_jogo()

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontuacao = 1000

    dificuldade_nivel = receber_nivel_dificuldade()
    total_tentativas = definir_numero_tentativas(dificuldade_nivel)

    for rodada in range(1, total_tentativas + 1):
        imprime_tentativas_restantes(rodada, total_tentativas)
        chute = receber_numero_chutado()

        if (chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100");
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Voce acerto!")
            print("Total de pontos: {0}".format(pontuacao))
            break
        else:
            if (maior):
                print("Voce errou! O chute foi maior que o numero secreto")
            elif(menor):
                print("Voce errou! O chute foi menor que o numero secreto")
            pontuacao -= abs(numero_secreto - chute)

    print("O numero secreto e: {0}".format(numero_secreto))
    print("Fim do jogo")

if __name__ == "__main__":
    jogar()