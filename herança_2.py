class Mae:
    def __init__(self, nome, ano):
        self._nome = nome.title()
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

    def __str__(self):  # Faz com que o objeto seja mostrado como string
        return ("Nome: {}, Ano: {}, Like: {} ".format(self.nome, self.ano, self._likes))





class Filme(Mae):
   def __init__ (self, nome, ano, duracao):
     super().__init__(nome, ano)
     self.duracao = duracao

   def __str__(self):
       return ("Nome: {}, Ano: {}, Duração: {}, Like: {} ".format(self.nome, self.ano, self.duracao, self._likes))



vingadores = Filme("querra infinita", "2010", "160")
vingadores.dar_like()
vingadores.dar_like()
vingadores.nome  = "homem de ferro"





class Serie(Mae):
    def __init__ (self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas  = temporadas

    def __str__(self):
        return ("Nome: {}, Ano: {}, Temporadas: {}, Like: {} ".format(self.nome, self.ano, self.temporadas, self._likes))

atlata = Serie("atlata", "2018", "10")
atlata.dar_like()
atlata.dar_like()
atlata.dar_like()
atlata.nome = "the office"
#print ("Nome: {}, Ano: {},Temporadas: {}, Like: {}".format(atlata.nome, atlata.ano, atlata.temporadas, atlata.likes))



class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]


    @property
    def listagem(self):
        return self._programas


    def __len__(self):
        return len(self._programas)


tmep = Filme ("todo mundo em panico",1999, 100)
tmep.dar_like()
tmep.dar_like()


filmes_e_series = [atlata, vingadores, tmep]

fim_de_semna = Playlist (filmes_e_series)
print(fim_de_semna[0])


for programa in filmes_e_series:
    print(programa)

