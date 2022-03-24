url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

url_base = url[0:url.find('?')]
print(url_base)

url_parametros = url[url.find('?')+1:]
print(url_parametros)
