from django.urls import path
from . import views

urlpatterns = [
    path ('list/', views.task_list, name='list'),
    path ('list/<param>', views.task_list, name='list'),
    path('addTask/', views.task ,name='task'),
    path('list/<param>', views.task_detail, name='detail'),
    ]