from blog.views import index, page, post, about, category
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:slug>/', post, name='post'),
    path('page/<slug:slug>/', page, name='page'),
    path('about/', about, name='about'),
    path('category/<slug:slug>/', category, name='category'),
]
