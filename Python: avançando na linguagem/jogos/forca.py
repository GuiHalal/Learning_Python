def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")
    palavra_secreta = "banana"
    letras_acertada = list("_" * len(palavra_secreta))
    print(letras_acertada)
    enforcou = False
    acertou = False
    while not enforcou and not acertou:
        chute = input("Qual a letra? ")
        chute = chute.strip()
        index=0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertada[index] = letra
                #print('Encontrei a letra "{}" na posição {}'.format(chute, index))

            index = index+1
        print(letras_acertada)
        print("jogando")

    print("Fim do jogo")
if (__name__ == "__main__"):
    jogar()