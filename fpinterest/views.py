from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import TemplateView, FormView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def explorar(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'explorar.html', context=context)


def detalhes_perfil(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    context = {'perfil': perfil}
    return render(request, 'perfil.html', context=context)


def detalhes_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'detalhes_posts.html', context=context)


def deletar_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('fpinterest:perfil', pk= request.user.id)

def deletar_perfil(request, pk):
    usuario = User.objects.get(pk=pk)
    usuario.delete()
    return redirect('fpinterest:explorar')


class CriarConta(FormView):
    template_name = 'forms/criar_conta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        user = form.save()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']  
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('fpinterest:editarfoto', kwargs={'pk': self.request.user.id})
    

class CriarPost(LoginRequiredMixin, FormView):
    template_name = 'forms/criar_post.html'
    form_class = CriarPostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.usuario = self.request.user 
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('fpinterest:perfil', kwargs={'pk': self.request.user.id})
    

class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'forms/editar_perfil.html'
    model = User
    fields = ['username', 'email']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.id != self.kwargs['pk']:
                return self.redirect_to_own_profile()
        else:
            return HttpResponseRedirect(reverse('fpinterest:login'))
        return super().dispatch(request, *args, **kwargs)

    def redirect_to_own_profile(self):
        own_profile_url = reverse('fpinterest:editarperfil', kwargs={'pk': self.request.user.id})
        return HttpResponseRedirect(own_profile_url)

    def get_success_url(self):
        return reverse('fpinterest:perfil', kwargs={'pk': self.request.user.id})


class EditarFotoPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'forms/editar_foto.html'
    model = Perfil
    fields = ['foto_perfil']

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.id != self.kwargs['pk']:
                return self.redirect_to_own_profile()
        else:
            return HttpResponseRedirect(reverse('fpinterest:login'))
        return super().dispatch(request, *args, **kwargs)

    def redirect_to_own_profile(self):
        own_profile_url = reverse('fpinterest:editarfoto', kwargs={'pk': self.request.user.id})
        return HttpResponseRedirect(own_profile_url)

    def get_success_url(self):
        return reverse('fpinterest:perfil', kwargs={'pk': self.request.user.id})
