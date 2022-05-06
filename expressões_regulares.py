endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"


import re   #Expressões regulares

padrao = re.compile ("[0-9]{5}[-]?[0-9]{3}") # O ponto de interrogação indica que o hífen pode ou não aparecer.
busca = padrao.search(endereco)  # Search indica se encontro o padrão. Que no caso é o cep.

if busca:
    cep =busca.group()  # O group vai retorna a string que foi encontrada no padrão.
    print(cep)




# Validador_url
# Exemplos de URLs válidas:


import re

url = 'https://www.bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')   # Verifica se a url é valida ou não
match = padrao_url.match(url)   # O MATCH verifica se bate exatamento com o padrão

if not match:
    raise ValueError("A URL não é válida.")

print("A URL é válida")


