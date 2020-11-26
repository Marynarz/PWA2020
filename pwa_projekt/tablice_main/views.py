from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


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
            return redirect('/index')
    else:
        form = UserCreationForm()
    return render(request, 'tablice_main/forms.html', {'form': form, 'method_name': 'Register'})


@login_required(login_url='/login')
def index(request):
    aval_boards = Board.objects.filter(owner_id=request.user.id)
    return render(request, 'tablice_main/user-home.html', {'logged_in': request.user.is_authenticated,
                                                           'boards': aval_boards})


def logout_view(request):
    logout(request)
    return render(request, 'tablice_main/base.html', {'content': 'LogOut succesfull'})


def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/index')
    return render(request, 'tablice_main/user-login.html')


@login_required(login_url='/login')
def create_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = Board(owner=request.user, board_name=form.cleaned_data.get('board_name'))
            board.save()
            return redirect('/index')
    else:
        form = BoardForm

    return render(request, 'tablice_main/forms.html', {'form': form, 'method_name': 'Create board'})