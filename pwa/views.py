from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import *


def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return HttpResponse(user)


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'pwa/UserReg.html', {'form': form})


def index(request):
    return render(request, 'pwa/index.html')


def logout_view(request):
    logout(request)
    return render(request, 'pwa/Base.html', {'content': 'LogOut succesfull'})


def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            pass
    else:
        pass
    return render(request, 'pwa/UserLogin.html')
