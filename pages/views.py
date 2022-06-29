from multiprocessing import context
from re import template
from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User 
from .models import Post
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import  PostForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


# Create your views here.
class IndexView(TemplateView):
    template_name = 'home.html'


class CadastroView(TemplateView):

    template_name = 'cadastro.html'


class LoginView(TemplateView):
    template_name = 'login.html'

class PostView(TemplateView):
    template_name = 'post-view.html'

# def teste(request):
#     return render(request, '')



def cadastro(request):# def para realizar o cadastro de um novo usuário
    context = {}
    context1 = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmacao_senha = request.POST.get('password-confirm')

        user = User.objects.filter(username=username).first() #uma consulta no banco de dados da aplicação para saber se o usuário ja está resistrado ou não

        if user:
            context['error'] = 'Usuário já registrado, escolha outro nome!'
        elif senha != confirmacao_senha:
            context['error'] = 'Senhas diferentes' 
        else:
            user = User.objects.create_user(username, email, senha) #O django tem um usuário padrão e tem a função de create_user, que facilita bastanta na hora de criar um usuário
            user.save()
            context1['certo'] = 'Cadastro Realizado com sucesso'
            return HttpResponseRedirect("/login", context1)

    return render(request, 'login/cadastro.html', context)




def logar(request): #def para realizar o login de um usuário já cadastrado
    context = {}

    if request.method == 'POST':

        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username = username, password = senha) #autentica dentro do banco o que está registrado e se essa é a senha correspondente

        if user:
            login(request, user)
            return render(request, 'home.html', context)
        else:
            context['error'] = 'Senha ou usuário invalidos'

    return render(request, 'login/login.html', context)

@login_required
def cadastro_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/home")
    else:
        form = PostForm()
    
    context = {
        'form': form
    }

    return render(request, 'controle/post.html', context)

def cadastrar_post(request): #def para realizar o login de um usuário já cadastrado
    context = {}

    if request.method == 'POST':

        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        endereco = request.POST.get('endereco')
        post = Post.objects.create(titulo=titulo, conteudo=conteudo, image  = endereco)
        return HttpResponse("Cadastro Realizado com sucesso")
        #return reverse("mostrar_post", kwargs = {'id':post.id}) #criar a url do post

    return render(request, 'controle/post.html', context)



@login_required
def editar_posts(request,post_id):

    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("")
    else:
        form = postForm(instance=post)
    
    context = {
        'form': form,
        'post_id': post_id
    }
    return render(request, 'controle/post.html', context)    


def editar_post(request, id): #def para realizar o login de um usuário já cadastrado
    context ={}
    context["data"] = Post.objects.get(id = id)
    obj = get_object_or_404(Post, id = id)

    if request.method == 'POST':
        obj.delete()
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        endereco = request.POST.get('endereco')
        post = Post(id = id,titulo=titulo, conteudo=conteudo,endereco = endereco)
        post.save()
        #return reverse("mostrar_post", kwargs = {'id':post.id}) #criar a url do post

    return render(request, 'controle/edit-post.html',context)


@login_required
def post_view(request):
    context = {}
 
    # add the dictionary during initialization
    context["dataset"] = Post.objects.all()
         
    return render(request, "controle/list-post.html", context)

@login_required
def user_view(request):
    context = {}
 
    # add the dictionary during initialization
    context["dataset"] = User.objects.all()
         
    return render(request, "controle/usuario.html", context)

@login_required
def detail_post(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Post.objects.get(id = id)
         
    return render(request, "controle/detail-post.html", context)    

@login_required
def detail_user(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = User.objects.get(id = id)
         
    return render(request, "controle/detail-user.html", context)    

@login_required
def delete_user(request, id):
    context ={}
    context["data"] = User.objects.get(id = id)
    obj = get_object_or_404(User, id = id)
    obj.delete()
    return render(request, "controle/usuario.html", context)
@login_required
def delete_post(request, id):
    context ={}
    context["data"] = Post.objects.get(id = id)
    obj = get_object_or_404(Post, id = id)
    obj.delete()
    return render(request, "controle/list-post.html", context)


def test(request):

    return render(request, "controle/usuario.html")

def sensorial(request):
    post = Post.objects.all()
    context = {
        'posts' : post
    }
    return render(request, "blog/sensorial.html", context)


def alfabetizacao(request):
    post = Post.objects.all()
    context = {
        'posts' : post
    }

    return render(request, "blog/alfabetizacao.html", context)

def coordenacao(request):
    post = Post.objects.all
    context = {
        'posts' : post
    }
    
    return render(request, "blog/coordenacao.html", context)


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'image.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'controle/image.html', {'form': form})