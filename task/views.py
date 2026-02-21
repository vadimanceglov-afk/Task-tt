from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Task
# Create your views here.

class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task/task_list.html"


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task/task_dataile.html"