from class_data_hora import DatasBr
from datetime import datetime, timedelta
import requests
from acesso_cep import BuscaEndereco


# cadastro = DatasBr()
# print(cadastro.dia_semana())
# print((cadastro.mes_cadastro()))

# hoje = datetime.today()
# hoje_formatada = hoje.strftime("%d/%m/%Y")
#
# print(hoje)
# print(hoje_formatada)

# cadastro = DatasBr()
# print(cadastro)

# hoje = DatasBr()
# print(hoje.tempo_cadastro())


# r = requests.get ("https://viacep.com.br/ws/01001000/json/")      #Usa o get para chamar o endereço.
# print(r.text)



cep = "25800320"
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)