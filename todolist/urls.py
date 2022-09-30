from todolist.views import *
from django.urls import path

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('create-task/', create_task, name='create-task'),
    path('logout/', logout, name='logout'),
]