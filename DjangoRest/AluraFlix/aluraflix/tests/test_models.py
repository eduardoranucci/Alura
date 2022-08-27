from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):

    def setUp(self):

        self.programa = Programa(
            titulo = 'Star Wars',
            data_lancamento = '1999-09-14'
        )

    def test_atributos(self):
        '''
        Verifica os atributos de um programa com valores default.
        '''

        self.assertEqual(self.programa.titulo, 'Star Wars')
        self.assertEqual(self.programa.data_lancamento, '1999-09-14')
        self.assertEqual(self.programa.tipo, 'F')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)