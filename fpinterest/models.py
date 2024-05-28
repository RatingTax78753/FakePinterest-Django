from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='foto-perfil', null=True, blank=True)

    def __str__(self):
        return f'Perfil: {self.usuario.username}'

class Post(models.Model):
    imagem = models.ImageField(upload_to='posts-images')
    titulo = models.CharField(max_length=120, null=True, blank=True)
    descricao = models.CharField(max_length=250, null=True, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return f'Post {self.id} | Autor: {self.usuario.username} | Título: {self.titulo}'
    