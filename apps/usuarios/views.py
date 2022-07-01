from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.http import HttpRequest, JsonResponse

from urllib.request import urlopen
import json

from usuarios.models import DadoPessoal, Estado

def cadastro(request):
    '''Cadastro de novo usuário no sistema'''
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        if campo_em_branco(nome):
            messages.error(request,'O campo nome não pode ficar em branco')
            return redirect('usuarios:cadastro')
        if campo_em_branco(email):
            messages.error(request,'O campo e-mail não pode ficar em branco')
            return redirect('usuarios:cadastro')
        if senhas_incorretas(senha,senha2):
            messages.error(request,'As senhas não são iguais')
            return redirect('usuarios:cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request,'E-mail já cadastrado')
            return redirect('usuarios:cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request,'Usuário já cadastrado')
            return redirect('usuarios:cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request,'Cadastro realizado com sucesso')
        return redirect('usuarios:login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    '''Controlo o acesso ao sistema'''
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_em_branco(email) or campo_em_branco(senha):
            messages.error(request,'Os campos e-mail e senha não podem estar em brancos')
            return redirect('usuarios:login')
        #print(email,senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username',flat=True).get()
            user = auth.authenticate(request,username=nome,password=senha)
            if user is not None:
                auth.login(request,user)
                #print('Login realizado com sucesso')
                return redirect('usuarios:dashboard')
        else:
            messages.error(request,'Usuário ou senha incorreta.')
    return render(request,'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if autenticado(request):
        id = request.user.id
        print(id)
        return render(request,'usuarios/dashboard.html')
    else:
        return redirect('index')

def autenticado(request):
    return request.user.is_authenticated

def campo_em_branco(campo):
    return not campo.strip()

def senhas_incorretas(senha, senha2):
    return senha != senha2

def pesquisa_cep(request):
    if request.method == 'POST':
        cep = request.POST['cep']
        url = "http://viacep.com.br/ws/"+cep+"/json"
        print('chamou pesquisa cep')
        print(cep)
        print(url)
        response = urlopen(url)
        data = json.loads(response.read())
        print(data)
        print(type(data))
        if data['uf'] == 'PE':
            print('CEP CORRETO')
            return JsonResponse(data)
        else:
            print('CEP INCORRETO')
            return JsonResponse(data)
    else:
        return render(request,'rede_social/via_cep.html')

