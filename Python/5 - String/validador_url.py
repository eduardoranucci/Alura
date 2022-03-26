import re

"""
bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio 
"""

# https://www.bytebank.com.br/cambio

url = 'https://www.bytebank.com.br/cambio'
url_padrao = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = url_padrao.match(url)

if not match:
    raise ValueError('A Url não é válida')

print('Url válida')
