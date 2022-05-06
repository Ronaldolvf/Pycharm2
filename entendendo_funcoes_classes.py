def test():

    print ("wellcome")
    informe_numero = int(input("defina o número"))

    if (informe_numero <= 10):
        print("errou")
    else:
        print ("acertou")

if (__name__ == "__main__"):                                                                                          # Quando se coloca o main, não se consegue importa com o from.
    test()

class ControleRemoto:

    def __init__(self, cor, altura, largura, espesura):
        self.cor = cor
        self.altura = altura
        self.largura = largura
        self.espesura = espesura

    def passa_canal(self, botao):
        if botao == "+":
            print("Aumenta canal")
        elif botao == "-":
            print("Diminuir canal")

    def __str__ (self):
        return ("cor:{} altura:{} largura:{} espesura:{} Marca: {}".format(self.cor, self.altura, self.largura,
                                                                           self.espesura, self.espesura))


class LG(ControleRemoto):

    def __init__(self, cor ,altura, largura, espesura, marca):
        super().__init__(cor, altura, largura, espesura)                                   # O "super(). é utilizado para  ultilizar métodos da classe da class mãe.
        self.marca = marca

    def __str__ (self):
        return ("cor:{} altura:{} largura:{} espesura:{} Marca: {}".format(self.cor, self.altura, self.largura,
                                                                           self.espesura, self.marca))

test = LG ("cinza", "10cm", "2cm", "3cm", "LG")
print(test)
test.passa_canal("+")


class Samsung(ControleRemoto):
    def __init__(self, cor ,altura, largura, espesura, marca):
        super().__init__(cor, altura, largura, espesura)      # O "super(). é utilizado para  ultilizar métodos da classe da class mãe.
        self.marca = marca

    def __str__(self):
        return ("cor:{} altura:{} largura:{} espesura:{} Marca: {}".format(self.cor, self.altura, self.largura,
                                                                           self.espesura, self.marca))

test = Samsung ("cinza", "10cm", "2cm", "3cm", "Samsung")
print(test)
test.passa_canal("-")


class Clientes:

    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.qualidade = "premium"
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print("Plano inválido")

    def mudar_pano(self, novo_plano):                                                                                   # Função feita para mudar de plano.
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("PLano Inválido.. Permanecer no premium")

    def qualidade_imagem(self, qualidade):
        if self.plano == self.qualidade:
            print("Qalidade HD")
        else:
            print("Tal qualidade não compativel com seu plano")

    def __str__(self):
        return ("Nome: {} e-amil: {} Plano: {}".format(self.nome, self.email, self.plano))


cliente = Clientes("lira", "lira@gmail", "premium")
print (cliente)

cliente.mudar_pano("basic")
print (cliente)

cliente.qualidade_imagem("")
