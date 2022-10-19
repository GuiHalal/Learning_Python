import random
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")

    #with open("palavras.txt") as arquivo:
     #   for linha in arquivo:
      #      print(linha)
    # REFATORAR PARA FICAR NO PADRAÃO ACIMA

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()


    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()

    #print(palavras)


    # List Comprehensions
    letras_acertadas = ["_" for letra in palavra_secreta]
    # metodo que eu bolei:
    # letras_acertadas = list("_" * len(palavra_secreta))
    print(letras_acertadas)
    tentativas = 6
    enforcou = False
    acertou = False

    erros = 0
    while not enforcou and not acertou:
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()
        if(chute in palavra_secreta):
            index=0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                    #print('Encontrei a letra "{}" na posição {}'.format(chute, index))
                index = index+1
        else:
            erros += 1
            if((6 - erros)>1):
                print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))
            elif((6 - erros)==1):
                print("Ops, você errou! ULTIMA TENTATIVA!")
        enforcou = erros == tentativas
        acertou = "_" not in letras_acertadas
        print("\n",  letras_acertadas, "\n")

    print("Fim do jogo")
    if(acertou):
        print("Vitória!")
    else:
        print("Que pena! Você foi enforcado!")
if (__name__ == "__main__"):
    jogar()