from django.contrib import admin
from django.urls import path, include
from Backend import views

urlpatterns = [
    path('todo-list/',views.TodoListView.as_view(),name='view'),
    path('todo-list-add/',views.TodoListView.as_view(),name='add'),
    path('todo-list-delete/<int:id>/', views.TodoListView.as_view(), name='todo-list-delete')
]
