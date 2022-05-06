class programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()  # Deixa as letras iniciais maiúsculas.
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


    def imprime(self):
        print ("Nome: {}, Ano: {}, Like: {}".format(self._nome, self.ano, self.likes))


# class Playlist:
#
#     def __init__(self, nome, programas):
#         self.nome = nome
#         self._programas = programas
#
#     def __getitem__(self, item):
#         return self._programas[item]
#
#
#     @property
#     def listagem(self):
#         return self._programas
#
#     @property
#     def tamanho(self):
#         return len(self._programas)



class Serie(programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome,ano)      # O "super(). é utilizado para  ultilizar métodos da classe da class mãe.
        self.temporada = temporada


    def imprime(self):  # Esta usado o polimorfismo para mofificar o imprimi da class mae.
        print("Nome: {}, Ano: {}, Temporada: {}, Likes:{}".format(self._nome, self.ano, self.temporada, self.likes))


atlanta = Serie("atlata", 2016, 2)
atlanta.dar_like()
atlanta.dar_like()




class Filme(programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print("Nome: {}, Ano: {},Duração: {}, Like: {}".format(self._nome, self.ano, self.duracao, self.likes))


vingadores = Filme ("querra infinita", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.nome = "vingadores"      # Para mudar o nome.



class Filme(programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print("Nome: {}, Ano: {},Duração: {}, Like: {}".format(self._nome, self.ano, self.duracao, self.likes))


tmep = Filme ("todo mundo em panico",1999, 100)
tmep.dar_like()
tmep.dar_like()






filmes_e_series = [vingadores, atlanta, tmep]     # Criando uma lista

#playlist_fim_de_semana =  Playlist (filmes_e_series)

for programa in filmes_e_series:
        #print(programa)
# detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporada     # O hasattr é utilizado para passar o objeto e o nome desse objeto.
    programa.imprime()

print(tmep in filmes_e_series)  # Verificar se o filme "tmep" está dentro da lista.


