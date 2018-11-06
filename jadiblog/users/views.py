from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse


# Create your views here.


class LoginView(LoginView):
    template_name = 'registration/login.html'

