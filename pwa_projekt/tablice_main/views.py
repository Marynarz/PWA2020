from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .app_defs import *


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


@login_required(login_url='/login')
def show_board(request, board_id):
    board = Board.objects.get(id=board_id)
    tables = Tab.objects.filter(board=board)
    elems = Element.objects.filter(tab__in=tables)
    ret_dict = {'board': board, 'tabs': tables, 'elems': elems}
    return render(request, 'tablice_main/board.html', ret_dict)


@login_required(login_url='/login')
def add_tab(request, board_id):
    if request.method == 'POST':
        last_tab = Tab.objects.filter(board__id=board_id).order_by('-position').values_list('position')
        if len(last_tab) == 0:
            last_tab = 0
        else:
            last_tab = last_tab[0][0]
        form = TabForm(request.POST)
        if form.is_valid():
            tab = Tab(board=Board.objects.get(id=board_id), tab_name=form.cleaned_data.get('tab_name'),
                      position=last_tab + 1)
            tab.save()
            return redirect('/board/%d' % board_id)
    else:
        form = TabForm

    return render(request, 'tablice_main/forms.html', {'form': form, 'method_name': 'Create tab'})


@login_required(login_url='/login')
def operate_objects(request, board_id=None, tab_id=None, elem_id=None):
    if request.method == 'POST':
        # Removing element or tab or board
        if request.POST['operation'] == POST_OPERATION_REMOVE:
            if elem_id:
                Element.objects.filter(tab__id=tab_id).get(id=elem_id).delete()
            elif tab_id:
                Tab.objects.filter(board__id=board_id).get(id=tab_id).delete()
            elif board_id:
                Board.objects.get(id=board_id).delete()
        return HttpResponse('OK')
    return HttpResponse('NOK')
