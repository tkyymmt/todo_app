from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def render_view(request):
    todos = Todo.objects.all()
    return render(request, 'todo.html', {'todos': todos})

def addTodo(request):
    todo = Todo(title=request.POST['title'])
    todo.save()
    return redirect('/todo')

def editTodo(request, id):
    todo = Todo.objects.filter(id=id)
    todo.title = request.POST['title']
    todo.update()
    return redirect('/todo')

def deleteTodo(request, id):
    todo = Todo.objects.filter(id=id)
    todo.delete()
    return redirect('/todo')