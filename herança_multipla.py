class Funcionario:

    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

    def __str__(self):
        return self.nome



class Caelum(Funcionario):

    def mostrar_tarefass(self):
        print('Fez muita coisa, Caelumer')


class Alura(Funcionario):

    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum.')



class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


# luan = Pleno('Luan')
# luan.busca_perguntas_sem_resposta()
# luan.mostrar_tarefas()
# luan.mostrar_tarefass()
# print(luan)
#
# ronaldo = Junior("Ronaldo")
# ronaldo.mostrar_tarefas()





