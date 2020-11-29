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
    path('board/<int:board_id>/', views.show_board, name='show_board'),
    path('board/<int:board_id>/new_tab', views.add_tab, name='add_tab'),
    path('board/<int:board_id>/<int:tab_id>/new_elem', views.add_elem, name='add_tab'),
    path('operation', views.operate_objects),
    path('operation/<int:board_id>', views.operate_objects),
    path('operation/<int:board_id>/<int:tab_id>', views.operate_objects),
    path('operation/<int:board_id>/<int:tab_id>/<int:elem_id>', views.operate_objects),
]