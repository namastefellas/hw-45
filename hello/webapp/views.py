from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task, status_choices
from django.http import HttpResponseRedirect

# Create your views here.

def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})

def task_view(request, pk):
    tasks = Task.objects.get(pk=pk)
    return render(request, 'task_view.html', context={'task': tasks})

def add_task(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'add_task.html',{'status':status_choices})
    elif request.method == "POST":
        title = request.POST.get("title")
        status = request.POST.get("status")
        description = request.POST.get("description")
        if not description:
            description=None
        time = request.POST.get("time")
        if not time:
            time=None

        task = Task.objects.create(
            title=title,
            status=status,
            time=time,
            description=description
        )
        return redirect('task_view', pk=task.pk)

    
def task_update_view(request, pk):
    tasks = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', context={'task': tasks})
    elif request.method == 'POST':
        tasks.title = request.POST.get('title')
        tasks.status = request.POST.get('status')
        tasks.time = request.POST.get('time')
        tasks.description = request.POST.get('description')
        return redirect('task_view', pk=tasks.pk)