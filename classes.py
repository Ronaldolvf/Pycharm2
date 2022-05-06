class Conta:                                                                           # Uma função que define receita que serve para vários objetos.

    def __init__(self, numero, titular, saldo, limite):                                # __imit__ é o inicializados.        # (numero, titular, saldo, limite) São atributos.
        #print("Construindo objeto...{}".format((self))                                 # Self é a referencia de onde está quardado o objeto para ser acessado.
        self.numero  = numero                                                          # Adicionar o __ faz com que a classe torna-se privado o atributo.
        self.titular = titular
        self.saldo   = saldo
        self.limite  = limite

    def __str__(self):
        return ("numero {} titular {} saldo {} limite {}".format(self.numero, self.titular,
                                                                 self.saldo, self.limite))

    def extrato(self):                                                                   # Criando métodos.
        print ("Saldo de R$:{} do titular {}".format(self.saldo, self.titular))

    def deposita (self, valor):
        self.saldo += valor

    def pode_sacar (self, valor_a_sacar):                                               # (__) deixa o método privado.
        valor_disponivel_a_sacar = self.saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca (self, valor):
        if (self.pode_sacar(valor)):
            self.saldo  -= valor
        else:
            print("o valor{} passou o limite".format(valor))

    def transfere (self, valor, destino):                                                 # ex: conta02.trandere(10.0, conta).
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo (self):                                                                 # O get retorna os dados.
        return self.limite

    def set_limite(self, limite):                                                         # (set) modifica o valor.
        self.limite == limite


    @property                                                                             # Substitue o get.  # Diferente do get, quem depende da classe não precisa mudar.
    def limite (self):
        return self.limite.title()                                                       # (title) aumenta a primeira letra da palavra.

    @limite.setter                                                                        # Substitue o o set.
    def limite (self, limite):
        self.limite = limite

    @staticmethod                                                                         # Criando um método estático.
    def codigos_bancos():
        return {"bb": "001", "caixa" : "104", "bradesco" : "237"}


# conta_corrente = Conta("001", "Ronaldo", "500", "1000")
# print(conta_corrente)
#
# print (conta_corrente.pode_sacar("400"))




