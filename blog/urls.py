from django.urls import path
from django.views.generic import ListView
from .views import Bloglist, BlogDetailView, About
from . import views

urlpatterns = [
    path('', Bloglist.as_view(), name='home'), #старый проект
    path('edu/', views.edu_list, name='edu_list'),
    path('agr/', views.agr_list, name='arg_list'),
    path('empl/', views.empl_list, name='empl_list'),
]