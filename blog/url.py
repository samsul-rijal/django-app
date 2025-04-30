from django.urls import path
from .views import user_create, dashboard, user_list, add_task, task_list


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('users/', user_list, name='users'),
    path('create-user/', user_create, name='user_form'),
    path('add-task/', add_task, name='add_task'),
    path('task-list/', task_list, name='task_list'),
]
