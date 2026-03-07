from django.shortcuts import render
from django.contrib.auth.views import LogoutView, LoginView

class LogoutUserView(LogoutView):
    next_page = "tasks:task-list"

class LoginUserView(LoginView):
    template_name = "auth_user/login.html"

#class RegisterUserView():
#    pass