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

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}'


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        
        super(Filme, self).__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao}min - Likes: {self._likes}'


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):

        super(Serie, self).__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self._likes}'


class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas


matrix = Filme('matrix', 2018, 160)
the_office = Serie('the office', 2005, 9)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

matrix.dar_like()
matrix.dar_like()
matrix.dar_like()
matrix.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
the_office.dar_like()
the_office.dar_like()
the_office.dar_like()

filmes_e_series = [matrix, the_office, demolidor, tmep]

playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)
