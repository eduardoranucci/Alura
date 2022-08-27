from django.test import TestCase
from aluraflix.models import Programa

class FixtureDataTestCase(TestCase):

    fixtures = ['programas_iniciais']

    # def setUp(self):
    #     pass 

    def test_carregamento_fixture(self):
        
        programa_bruxo = Programa.objects.get(pk=2)
        todos_os_programas = Programa.objects.all()

        self.assertEqual(programa_bruxo.titulo, 'O bruxo')
        self.assertEqual(len(todos_os_programas), 9)