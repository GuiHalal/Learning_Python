import random
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    total_de_tentativas = 0
    pontos = 1000
    nivel = 0

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    while(nivel>3 or nivel <1):
        nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    #numero_secreto = round(random.random() * 100)
    random.seed(random.random())
    numero_secreto = random.randrange(1, 101)

    acertou = False

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("\nVocê acertou! Sua pontuação foi {}.".format(pontos))
            acertou = True
            break
        else:
            if(maior):
                print("Você errou! {} é MAIOR do que o número secreto.".format(chute))
            elif(menor):
                print("Você errou! {} é MENOR do que o número secreto.".format(chute))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    if(acertou == False):
        print("\nQue pena! O número secreto era {}. "
              "Sua pontuação foi {}.".format(numero_secreto, pontos))
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()