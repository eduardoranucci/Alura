from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal

class IndexViewTestCase(TestCase):

    def setUp(self):
        
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'Gato',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Sim'
        )

    def test_index_retorna_resultado_animal(self):
        '''
        Verifica se a index retorna as características do animal pesquisado.
        '''

        response = self.client.get('/',
            {'buscar': 'Gato'}
        )

        animal_pesquisado = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(animal_pesquisado[0].nome_animal, 'Gato')
