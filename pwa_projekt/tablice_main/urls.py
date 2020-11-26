from django.urls import path

from . import views

app_name = 'tablice'
urlpatterns = [
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('registration/', views.register_user, name='register_user'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('new_board/', views.create_board, name='new_board'),
]