import re


class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url(url)

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self, url):
        if not url:
            raise ValueError('A url está vazia')

        url_padrao = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = url_padrao.match(url)

        if not match:
            raise ValueError('A Url não é válida')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_valor = self.get_url_parametros().find(parametro_busca) + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor


extrator = ExtratorUrl("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")

valor_quantidade = extrator.get_valor_parametro('quantidade')
print(valor_quantidade)
