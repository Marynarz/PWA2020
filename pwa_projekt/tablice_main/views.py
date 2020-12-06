from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .app_defs import *
import datetime


def start_page(request):
    if request.user.is_authenticated:
        return redirect('/index')
    elif request.method == 'POST':
        if 'log_user' in request.POST:
            form = AuthenticationForm(None, request.POST, prefix='login')
            if form.is_valid():
                username = request.POST['login-username']
                password = request.POST['login-password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/index')

        elif 'reg_user' in request.POST:
            form = UserCreationForm(request.POST, prefix='register')
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/index')
    else:
        form_register = UserCreationForm(prefix='register')
        form_login = AuthenticationForm(prefix='login')
    return render(request, 'tablice_main/start.html', {'form_register': form_register, 'form_login': form_login})


@login_required(login_url='')
def index(request):
    aval_boards = Board.objects.filter(owner_id=request.user.id)
    form = BoardForm()
    return render(request, 'tablice_main/user-home.html', {'logged_in': request.user.is_authenticated,
                                                           'boards': aval_boards,
                                                           'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'tablice_main/base.html', {'content': 'LogOut succesfull'})


@login_required(login_url='')
def show_board(request, board_id):
    # drzewo obiektow
    board = Board.objects.get(id=board_id)
    tables = Tab.objects.filter(board=board).order_by('position')
    elems = Element.objects.filter(tab__in=tables).order_by('create_time')

    # formularze
    tab_form = TabForm()
    elem_form = TaskForm()

    # slownik do zwrocenia
    ret_dict = {'board': board, 'tabs': tables, 'elems': elems, 'logged_in': request.user.is_authenticated,
                'form_tab': tab_form, 'form_elem': elem_form }
    return render(request, 'tablice_main/board.html', ret_dict)


@login_required(login_url='')
def operate_objects(request, board_id=None, tab_id=None, elem_id=None):
    print(request)
    if request.method == 'POST':
        # Removing element or tab or board
        if request.POST['operation'] == POST_OPERATION_REMOVE:
            if elem_id:
                Element.objects.filter(tab__id=tab_id).get(id=elem_id).delete()
            elif tab_id:
                Tab.objects.filter(board__id=board_id).get(id=tab_id).delete()
            elif board_id:
                Board.objects.get(id=board_id).delete()
        # Adding objects
        elif request.POST['operation'] == POST_OPERATION_ADD:
            post_dict = request.POST.dict()
            if elem_id is None and board_id is not None and tab_id is not None:
                elem = Element(tab=Tab.objects.get(id=tab_id), creator=request.user,
                               elem_name=post_dict['form[1][value]'],
                               description=post_dict['form[2][value]'])
                elem.save()
            elif tab_id is None and board_id is not None:
                last_tab = Tab.objects.filter(board__id=board_id).order_by('-position').values_list('position')
                if len(last_tab) == 0:
                    last_tab = 0
                else:
                    last_tab = last_tab[0][0]
                tab = Tab(board=Board.objects.get(id=board_id), tab_name=post_dict['form[1][value]'],
                          position=last_tab + 1)
                tab.save()
            elif board_id is None:
                board = Board(owner=request.user, board_name=post_dict['form[1][value]'],
                              description=post_dict['form[2][value]'])
                board.save()
        return HttpResponse('OK')
    return HttpResponse('NOK')


@login_required(login_url='')
def set_tab_postion(request, board_id):
    _ = board_id
    positions = request.POST.getlist('tab[]')
    pos_no = 1

    for tab in positions:
        last_tab = Tab.objects.get(id=tab)
        last_tab.position = pos_no
        last_tab.save()
        pos_no += 1

    return HttpResponse('OK')

