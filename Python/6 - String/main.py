url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

# sanitizacao da url
url = url.replace(' ', '')

if url == '':
    raise ValueError('A url está vazia')

# separa a url base e os parametros
url_base = url[:url.find('?')]
print(url_base)

url_parametros = url[url.find('?')+1:]
print(url_parametros)

# busca um parametro
parametro_busca = 'moedaDestino'
indice_valor = url_parametros.find(parametro_busca) + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
