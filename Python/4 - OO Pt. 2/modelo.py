class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()


class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()


vingadores = Filme('vingadores: guerra infinita', 2018, 160)
vingadores.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}min - Likes: {vingadores.likes}')

the_office = Serie('the office', 2005, 9)
the_office.dar_like()
the_office.dar_like()

print(f'Nome: {the_office.nome} - Ano: {the_office.ano} - '
      f'Temporadas: {the_office.temporadas} - Likes: {the_office.likes}')
