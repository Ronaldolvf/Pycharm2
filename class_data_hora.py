from datetime import datetime, timedelta

class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro (self):
        meses_do_ano = [
             "", "janeiro", "fevereiro", "março",       # Coloca o "" para indicar o número zero.
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month      # Apresenta o mes que foi cadastrado o código.
        return meses_do_ano[mes_cadastro]


    def dia_semana (self):
        dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta"
        ]

        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]


    def formart_data (self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y")      # Retornando a data completa
        return data_formatada


    def __str__(self):
        return self.formart_data()      # Evita de ter que chamar a função formart_data() quando for da print.

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days = 30) )  -self.momento_cadastro    # Retorna o tempo cadastrado
        return tempo_cadastro


print (DatasBr())
