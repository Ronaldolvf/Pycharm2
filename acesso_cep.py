import requests
class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise  ValueError ("Cep inválido")


    def cep_e_valido (self, cep):
        if len (cep) == 8:
            return True
        else:
            return  False


    def format_cep (self):
        return "{}-{}".format(self.cep[:5],self.cep[5:])


    def __str__(self):
        return self.format_cep()


    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/20735280/json/"
        r = requests.get (url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )

test = BuscaEndereco("20735280")
print (test.format_cep())
print(test.acessa_via_cep())
