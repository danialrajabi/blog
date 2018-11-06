from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# Create your views here.


class UsersLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'registration/login.html'
