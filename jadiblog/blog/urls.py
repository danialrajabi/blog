from django.urls import path,re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog', views.BlogListView.as_view(), name='blogpage'),
    path('post/create', views.PostCreateView.as_view(), name='create_post'),
    re_path('^post/update/(?P<slug>[^/]+)/?$', views.PostUpdateView.as_view(), name='update_post'),
    re_path('^post/(?P<slug>[^/]+)/?$', views.PostDetail.as_view(), name='post_detail'),

]
