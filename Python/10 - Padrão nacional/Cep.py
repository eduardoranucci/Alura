import requests


class addressSearch:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_is_valid(cep):
            self.cep = cep
        else:
            raise ValueError('A cep must have 8 digits.')

    def __str__(self):
        return self.format_cep()

    def cep_is_valid(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def acess_via_cep(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        request = requests.get(url)
        data = request.json()
        return (
            data['bairro'],
            data['localidade'],
            data['uf']
        )

