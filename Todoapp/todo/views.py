from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('index')
    return HttpResponse("Method not allowed", status=405)

def delete_task(request):
    if 'task_id' in request.GET:
        task_id = request.GET.get('task_id')
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return redirect('index')
        except Task.DoesNotExist:
            return HttpResponse("Task not found", status=404)
    return HttpResponse("Bad request", status=400)

def complete_task(request):
    if 'task_id' in request.GET:
        task_id = request.GET.get('task_id')
        try:
            task = Task.objects.get(id=task_id)
            task.completed = True
            task.save()
            return redirect('index')
        except Task.DoesNotExist:
            return HttpResponse("Task not found", status=404)
    return HttpResponse("Bad request", status=400)
