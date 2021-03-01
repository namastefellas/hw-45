from django.shortcuts import render
from webapp.models import Task, status_choices
from django.http import HttpResponseRedirect

# Create your views here.

def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})

def task_view(request, pk):
    tasks = Task.objects.get(pk=pk)
    return render(request, 'task_view.html', context={'task': tasks})

def add_task(request):
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

        return HttpResponseRedirect(f'/task/?id={task.id}')