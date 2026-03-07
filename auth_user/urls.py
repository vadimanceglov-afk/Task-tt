from django.urls import path
from . import views

urlpatterns = [
    path("logout/", views.LogoutUserView.as_view(), name="logout"),
    path("login/", views.LoginUserView.as_view(), name="login"),
]