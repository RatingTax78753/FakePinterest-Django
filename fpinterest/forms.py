from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms


class CriarContaForm(UserCreationForm):
    email = forms.EmailField()
    foto_perfil = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'foto_perfil')

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.email = self.cleaned_data['email']
        if commit:
            usuario.save()
            if 'foto_perfil' in self.cleaned_data:
                foto_perfil = self.cleaned_data['foto_perfil']
            else:
                foto_perfil = None
            Perfil.objects.create(usuario=usuario, foto_perfil=foto_perfil)
        return usuario

class CriarPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('imagem', 'titulo', 'descricao')