# Expressões regulares. Serva para encontrar padrões.

import re
#
# padrao = "[0-9][a-z][0-9]"
# texto = "123 1a2 1cc aa1"
# resposta = re.search(padrao, texto)                  # Buscando no texto o padrão informado.
#
# print(resposta.group())                              # O group() serve para incurta a resposta.


# padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"         # O \w serve para letras e númeoros.
# texto = "aaabbbcc rodrigo123@gmail.com.br"
# resposta = re.search(padrao, texto)                  # Buscando no texto o padrão informado.
#
# print(resposta.group())


# padrao_molde = "(xx)aaaa-wwww"
# padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"               #  "[0-9]" é ultilizado para números.    # {} inddica o número de repetições que deve ter.
# texto = "eu gosto do numero 2125944180"
# resposta = re.findall(padrao, texto)                # Diferente do search , o findall retorna todas as correspondencia que foram encontradas no texto.
#
# print(resposta)                                     # Com o findall não precisa coolocar o .group().



from TelefonesBr import TelefonesBr
import re

telefone = "552126481234"

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)


# padrao = "([0-9]{2,3})?:([0-9]){2})([0-9]{4,5})([0-9]{4})"      # Comn o ? se pode passsar com ou sem o número.
# resposta = re.findall(padrao,telefone)
# print(re.findall(padrao, telefone))



from TelefonesBr import TelefonesBr
import re

telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)


#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())
