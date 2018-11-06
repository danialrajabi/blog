from django.urls import path,re_path
from . import views

app_name = 'users'

urlpatterns = [
    path('login', views.UsersLoginView.as_view(), name='login'),
    path('logout', views.UsersLogoutView.as_view(), name='logout'),

]
