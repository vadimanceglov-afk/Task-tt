from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task-list"),
    path("<int:pk>/", views.TaskListView.as_view(), name="task-detail"),
]