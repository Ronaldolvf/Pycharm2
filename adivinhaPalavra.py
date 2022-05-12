import random       # random é um modulo/blibioteca que sabe gerar um número aleatório.

def jogar():        # É uma função

    mensagens_de_boas_vindas()


    arquivo = open ("programa.txt", "r")        # Abrir com leitura (r) o programa.
    programa = []                               # Inserindo o programa em uma lista.

    for linha in arquivo:
        linha = linha.strip()       # Para remover os espaços e as caractécries.
        programa.append(linha)      # Adiciona um elemento ao final da lista.

    arquivo.close()                 # Para ffechar o aquivo aberto.

    numero = random.randrange (0,len(programa))         # randrange é uma função utilizada para gerar um número aleatório. # len é utilizada para contar o número de palavras da lista.
    palavra_secreta = programa [numero].upper()



    letras_acertadas = ["_" for letra in palavra_secreta]       # Para preencher o espaço vazio com as letras da paçavra secreta.

    enforcou = False
    acertou  = False
    erros    = 0
    print(letras_acertadas)

    while (not enforcou and not acertou):


        chute = esse_e_o_chute()   # Recebe a função que está armazenado o chute.

        if (chute in palavra_secreta):
            index = 0

            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1
            desenha_forca(erros)


        enforcou = erros == 7
        acertou  = "_" not in letras_acertadas


        print (letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()

    else:
        imprime_mensagem_perdedor(palavra_secreta)







def mensagens_de_boas_vindas():  # Criar uma função para deixar o cógigo mais organizado
    print ("Bem vindooooooooooooooooooooooooooooooooooooooo")


def esse_e_o_chute():
    chute = input("Qual é a letra?")
    chute = chute.strip().upper()   # .strip() É usada para remover espaços em branco e caractéries especiais das palavras digitadas. # .upper considera o chute e a letra como maiúscula.
    return chute





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

def desenha_forca(erros):

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    elif(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    elif(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    elif(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    elif(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    elif(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    elif (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")







if (__name__ == "__main__"):
    jogar()
