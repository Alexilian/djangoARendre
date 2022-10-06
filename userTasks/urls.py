from django.urls import path
from . import views

urlpatterns = [
    path ('list/', views.task_list, name='list'),
    path ('list/<param1>/<param2>/', views.task_list, name='list'),
    path('addTask/', views.task ,name='task'),
    path('editTask/<param>/', views.task_edit ,name='task'),
    path('tacheDetail/<param>/', views.task_detail, name='detail'),
    path ('users/', views.user_list, name='list'),
    path('addUser/', views.user ,name='task'),
    path ('users/<param1>/<param2>/', views.user_list, name='list'),
    ]