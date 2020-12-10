from django.urls import path

from . import views

app_name = 'tablice'
urlpatterns = [
    path('', views.start_page),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('board/<int:board_id>/', views.show_board, name='show_board'),
    path('operation', views.operate_objects),
    path('operation/<int:board_id>', views.operate_objects),
    path('operation/<int:board_id>/<int:tab_id>', views.operate_objects),
    path('operation/<int:board_id>/<int:tab_id>/<int:elem_id>', views.operate_objects),
    path('position/tab/<int:board_id>', views.set_tab_postion),
    path('position/elem/', views.set_elem_postion)
]