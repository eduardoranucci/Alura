class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        
        super(Filme, self).__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):

        super(Serie, self).__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('vingadores: guerra infinita', 2018, 160)
vingadores.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}min - Likes: {vingadores.likes}')

the_office = Serie('the office', 2005, 9)
the_office.dar_like()
the_office.dar_like()

print(f'Nome: {the_office.nome} - Ano: {the_office.ano} - '
      f'Temporadas: {the_office.temporadas} - Likes: {the_office.likes}')
