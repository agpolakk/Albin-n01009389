from django.urls import path
from .views import *

urlpatterns = [
    path('', todo_list, name='todo-list'),
    path('api/todos/', TodoItemListCreate.as_view(), name='todo-list-create'),
    path('api/todos/<int:pk>/', TodoItemRetrieveUpdateDestroy.as_view(), name='todo-detail'),
]
