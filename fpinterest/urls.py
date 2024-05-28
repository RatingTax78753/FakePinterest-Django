from django.urls import path, reverse_lazy
from .views import *
from django.contrib.auth import views as auth_view

app_name = 'fpinterest'

urlpatterns = [
    path('', homepage, name="homepage"),
    path('explorar/', explorar, name="explorar"),
    path('post/<int:pk>/', detalhes_post, name="detalhespost"),
    path('perfil/<int:pk>/', detalhes_perfil, name="perfil"),
    path('criarpost/', CriarPost.as_view(), name='criarpost'),
    path('criarconta/', CriarConta.as_view(), name='criarconta'),
    path('login/', auth_view.LoginView.as_view(template_name='forms/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='forms/logout.html'), name='logout'),
    path('editar/perfil/<int:pk>/', EditarPerfil.as_view(), name='editarperfil'),
    path('perfil/foto/<int:pk>/', EditarFotoPerfil.as_view(), name='editarfoto'),
    path('changepassword/', auth_view.PasswordChangeView.as_view(template_name='forms/mudar_senha.html', success_url=reverse_lazy('fpinterest:explorar')), name='mudarsenha'),
    path('post/<int:pk>/deletar/', deletar_post, name='deletarpost'),
    path('perfil/<int:pk>/deletar/', deletar_perfil, name='deletarperfil'),
]