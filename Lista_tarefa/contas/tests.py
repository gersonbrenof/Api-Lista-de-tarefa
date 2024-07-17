from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from contas.models import Usuario
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from jwt import decode, InvalidTokenError
class ListaUsuariosTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Use o nome da URL reversa correto para listar usuários
        self.url = reverse('cadastrar-list')

    def test_listar_usuarios(self):
        Usuario.objects.create(username='user1', email='user1@example.com', password='password1')
        Usuario.objects.create(username='user2', email='user2@example.com', password='password2')
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
class CustomTokenObtainPairViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'testuser'
        self.email = 'testuser@example.com'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, email=self.email, password=self.password)

    def test_custom_token_obtain_pair_view(self):
        # Faça uma solicitação POST para obter um token JWT
        response = self.client.post('/api/token/', {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 200)

        # Verifique se o token JWT está presente na resposta
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

        # Extraia o token de acesso JWT da resposta
        access_token = response.data['access']

        # Verifique se o token JWT é válido decodificando-o
        try:
            decoded_access_token = decode(access_token, verify=False)
        except InvalidTokenError:
            self.fail("O token de acesso JWT não é válido")

        # Verifique se os campos personalizados estão presentes no token JWT
        self.assertEqual(decoded_access_token['username'], self.username)
        self.assertEqual(decoded_access_token['email'], self.email)
