from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lista.api.views import ListaViewSet, ListaAPIView
from contas.api.views import RegisterAPI, LoginApi
from knox import views as knox_views

from rest_framework_simplejwt.views import TokenRefreshView

# Criando um router para gerenciar as URLs da API de forma automática
router = DefaultRouter()

# Registrando os viewsets da sua API com o router
# router.register('api/cadastrar', UsuariosViewSet, basename='cadastrar')

# Adicionando as URLs personalizadas ao router
#router.register("api/Lista", ListaViewSet, basename="lista")

# Definindo as URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cadastrar/', RegisterAPI.as_view(), name='cadastrar'),
    path('api/login/', LoginApi.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/Listas/', ListaAPIView.as_view(), name='lista'),
    
    path('', include(router.urls)),  # Adicionando as URLs geradas pelo router
]
