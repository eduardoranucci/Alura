from django.test import TestCase
from django.urls import reverse
from animais.views import index
from django.test import RequestFactory

class AnimaisURLSTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
    
    def test_url_utiliza_view_index(self):
        '''
        Testa se a home do app utiliza a função index da view.
        '''
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
