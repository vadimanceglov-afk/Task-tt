from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Task
from task.form import TaskForm
# Create your views here.

class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task/task_list.html"


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task/task_dataile.html"

class TaskCreateView(CreateView):
    model = Task
    template_name = "task/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")