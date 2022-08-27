from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):

    def setUp(self):
        
        self.programa = Programa(
            titulo = 'Star Wars',
            data_lancamento = '1999-09-14',
            tipo = 'F',
            likes = 2665,
            dislikes = 25
        )

        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_campos_serializados(self):
        '''
        Verifica os campos que estão sendo serializados.
        '''

        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo', 'data_lancamento', 'tipo', 'likes']))

    def test_conteudo_serializado(self):
        '''
        Verifica os conteúdos que estão sendo serializados.
        '''

        data = self.serializer.data

        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)