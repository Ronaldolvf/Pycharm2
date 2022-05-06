# Lembrando que funções built-in são aquelas que você não precisa importar explicitamente, pois elas estão disponíveis para seu uso automaticamente.

import random  # random é um modulo/blibioteca que sabe gerar um número aleatório.


def numero():

    mensagens_de_boas_vindas()

    numero_secreto = random.randrange(1, 101)  # O randrange vai busca um número aleatório de 1 a 100.

    # total_de_tentativas = 1
    # total_de_tentativas = 0  # Não precisa criar a variável pois já a define abaixo.

    nivel = int(input("Defina o nível de dificuldade:"))

    if (nivel == 1):
        total_de_tentativas = 2000000000000000000000000

    elif (nivel == 2):
        total_de_tentativas = 10

    elif (nivel == 3):
        total_de_tentativas = 5




    # while (total_de_tentativas <= 3):
    for rodado in range(1, total_de_tentativas + 1):  # While and for vai executar a função enquanto ser verdadeira.

        chute_str = input("Digite o seu número:")

        print("Vc digitou", chute_str)


        chute = int(chute_str)      # Tranfomra a str em int (número).

        if (chute < 1 or chute > 100):
            print("Vc deve digitar o número entre 1 e 100")
            continue  # Continue apenas pula para próxima iteração


        acertou = chute == numero_secreto   # Uma variável do tipo bool pode ter apenas dois valores, True ou False
        maior   = chute  > numero_secreto
        menor   = chute  < numero_secreto



        if (acertou):
            imprime_mensagem_vencedor()
            break

        elif (maior):
            print("O chute foi maior")

        elif (menor):
            print("O chute foi menor")

    else:
        imprime_mensagem_perdedor(numero_secreto)









def mensagens_de_boas_vindas():  # Criar uma função para deixar o cógigo mais organizado
    print ("Bem vindoooo!!!")

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

def imprime_mensagem_perdedor(numero_secreto):
    print("Puxa, você foi enforcado!")
    print("O número era: {}".format(numero_secreto))
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


if (__name__ == "__main__"):
    numero()


