from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# Create your views here.

def index(request):
    context = {}
    template = 'todo_home.html'

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()


    context['Todos'] = Todo.objects.all
    context['form'] = form
    
    return render (request, template, context)

def updateView(request, pk):
    template='todo.html'
    context = {}
    todo = get_object_or_404(Todo, id=pk)
    
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context["form"]=form
   
    return render(request, template, context)

def deleteView(request, pk):
    context = {}
    template='delete_view.html'

    todo = get_object_or_404(Todo, id=pk)

    if request.method =='POST':
        todo.delete()
        return HttpResponseRedirect('/')
    
    context["todo"]= todo

    return render(request, template, context)