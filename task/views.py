from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
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

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "task/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")

class TaskDeletView(DeleteView):
    model = Task
    template_name = "task/task_delete.html"
    success_url = reverse_lazy("tasks:task-list")
