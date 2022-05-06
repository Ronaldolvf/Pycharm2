url = "https://twitter.com/home?langen=dolar@real"
url = url.replace(" ", "")                            # Vai substituir os espaços em branco.

base_url =url [0 : 19]
print(base_url)



indice_interrogacao = url.find("=")                  # O método "find" é utilizado para encontra um caractere dentro de uma string  # Imprime do parametro até antes a string indicada.
url_base =  url [0 : indice_interrogacao]
print(url_base)


url_paramentro = url [indice_interrogacao+1 :]      # Imprime tudo depois do parametro mais 1.
print(url_paramentro)


parametro_busca = "langen"
indice_parametro = url_paramentro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_tirar_resto = url_paramentro.find("com", indice_valor)

if indice_tirar_resto == -1 :
    valor = url_paramentro[indice_valor :]

else:
    valor = url_paramentro[indice_valor:indice_tirar_resto]


print(valor)




