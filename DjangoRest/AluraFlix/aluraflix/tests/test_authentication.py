from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class AuthenticationsUserTestCase(APITestCase):
    
    def setUp(self):
        
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password='r2d2')

    def test_autenticacao(self):
        '''
        Verifica a autenticação de um usuário com as credenciais corretas.
        '''
        user = authenticate(username='c3po', password='r2d2')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        '''
        Verifica uma requisição GET não autorizada.
        '''
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_username_incorreto(self):
        '''
        Verifica a autenticação de um usuário com o username incorreto.
        '''
        user = authenticate(username='darth-vader', password='padme')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_password_incorreto(self):
        '''
        Verifica a autenticação de um usuário com o password incorreto.
        '''
        user = authenticate(username='c3po', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_autorizada(self):
        '''
        Verifica uma requisição GET autorizado.
        '''
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)