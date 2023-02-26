from django.urls import path

from .views import render_view, addTodo, deleteTodo

urlpatterns = [
    path('', render_view),
    path('add', addTodo),
    path('delete/<int:id>', deleteTodo),
]