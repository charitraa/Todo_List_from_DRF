from django.contrib import admin
from django.urls import path, include
from Backend import views

urlpatterns = [
    path('todo-list/',views.todo_view,name='view'),
    path('todo-list-add/',views.todo_add,name='add'),
    path('todo-list-delete/<str:id>/', views.todo_delete, name='delete')
]
