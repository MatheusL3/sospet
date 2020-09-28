from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_protect


def login_user(request):
    return render(request,'login.html')


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'{username} and {password}')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválido. Favor tentar novamente!')
    return redirect('/login/')

@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')


def logout_user(request):
    logout(request)
    return redirect('/login/')