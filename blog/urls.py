from django.urls import path
from django.views.generic import ListView
from .views import Bloglist, BlogDetailView, About
from . import views

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), #старый проект
    path('about/', About.as_view(), name='about'), #старый проект
    path('', Bloglist.as_view(), name='home'), #старый проект
    path('edu/', views.edu_list, name='edu_list'),
]