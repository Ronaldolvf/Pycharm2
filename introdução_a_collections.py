class Conta_corrente:

    def __init__ (self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita (self, valor):
        self.saldo += valor

    def __str__(self):
        return ("Codigo {} saldo {}".format(self.codigo, self.saldo))


# conta_da_dani = Conta_corrente(80)                                          # Informa o número da conta.
# conta_da_dani.deposita(200)                                                 # Informa o valor depositado.
#
# conta_do_gui  = Conta_corrente(70)
# conta_do_gui.deposita(100)
#
#
# contas = [conta_da_dani, conta_do_gui]
# for clientes in contas:
#     print(clientes)
#
# def deposita_paara_contas (contasss):
#     for conta in contasss:
#         conta.deposita(500)
#
# deposita_paara_contas(contas)
# #print(contas[0], contas[1])
#
# conta_da_dani
# print ("Conta da Dani: {}".format(conta_da_dani))
#
# conta_do_gui
# print ("Conta do Gui: {}".format(conta_do_gui))



#Ex: guilherme = (guilherme , 37)    # Quando se coloco entre parenteses, se caracteriza como uma "tupla". Assim se tornado imutável.
# OBS: As listas tende a levar para o lado orientado objeto.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# <<Hereança e polimorfismo>>
# class Conta:
#
#     def __init__ (self, codigo):
#         self.codigo = codigo
#         self.saldo = 0
#
#     def deposita (self, valor):
#         self.saldo += valor
#
#     def __str__ (self):
#         return ("Codigo {} saldo {}".format(self.codigo, self.saldo))
#
#
# class ContaCorrente(Conta):
#
#     def passa_o_mes (self, saldo):
#         self.saldo -= saldo
#
# class ContaPoupanca (Conta):
#
#     def passa_o_mes (self, saldo):
#         self.saldo *= 2
#         self.saldo -= saldo
#
# conta16 = ContaCorrente(16)                                                 # Chamando a função conta corrente.
# conta16.deposita(500)
# conta16.passa_o_mes(600)                                                     # Usando a função passa_o_mes e informando o valor gasto no mes.
# print(conta16)
#
# conta17 = ContaPoupanca(16)                                                 # Chamando a função conta poupança.
# conta17.deposita(1000)
# conta17.passa_o_mes(1500)
# print(conta17)
#
#
# #Criando uma nova conta
#
# class Conta_salario:
#
#     def __init__ (self, codigo):
#         self.codigo = codigo
#         self.saldo = 0
#
#     def __eq__ (self, outro):                                                # Está chamndo a função de eguidade e é utilizada para comparar as contas
#         return self.codigo == outro.codigo and self.saldo == outro.saldo
#
#
#     def deposita (self, valor):
#         self.saldo += valor
#
#     def __str__ (self):
#         return ("Codigo {} saldo {}".format(self.codigo, self.saldo))
#
#
# conta1 = Conta_salario (37)
# conta1.deposita(100)
#
# conta2 = Conta_salario (37)
# conta2.deposita(100)
#
# print (conta1, conta2)
#
# ver = conta1 == conta2                                                    # Para verificar a eguidade
# print(ver)

# #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# idades = [15, 87, 32, 65, 56, 32, 49, 37]
#
# for i in range(len(idades)):
#   print(i)
#
# for indice, idade in enumerate(sorted(idades)):                                   # O enumerate devolve um número e o elemento    # Serve para coloca em ordem crecente mais não alterando a lista principal.
#     print(indice, "-", idade)
#
#
# usuarios = [
#     ("Guilherme", 37, 1981),
#     ("Daniela", 31, 1987),
#     ("Paulo", 39, 1979)
# ]
#
# for nome, idade, nascimento in usuarios:                                 # ja desempacotando    # As tuplas 3 elementos
#   print(nome, nascimento)

# #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class ContaSalario(Conta_corrente):  # Importando da class Conta_corrente.
    pass


conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(100)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(400)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]


def extrai_saldo(conta):
    return conta.saldo


for contass in sorted(contas,
                      key=extrai_saldo):  # sorted(contas, key=extrai_saldo) Organizando de forma crecente o saldo das conta.
    print(contass)
