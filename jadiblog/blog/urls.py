from django.urls import path,re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog', views.BlogListView.as_view(), name='blogpage'),
    re_path('^post/(?P<slug>[^/]+)/?$', views.PostDetail.as_view(), name='post_detail'),

]
