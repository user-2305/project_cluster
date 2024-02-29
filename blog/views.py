from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView #старый проект
from .models import Post, Edu
from .forms import RegionFilterForm

# Create your views here.
class BlogDetailView(DetailView): #старый проект
    model = Post
    template = 'post_detail.html'

class Bloglist(ListView): #старый проект
    model = Post
    template_name = 'home.html'

class About(TemplateView): #старый проект
    template_name = 'about.html'

'''
def edu_list(request):
    edus = Edu.objects.all()
    return render(request, 'edu_list.html', {'edus': edus})
'''

'''
def edu_list(request):
    form = RegionFilterForm(request.GET)
    if form.is_valid():
        region = form.cleaned_data['region']
        edus = Edu.objects.filter(region__icontains=region)
    else:
        edus = Edu.objects.all()
    return render(request, 'edu_list.html', {'edus': edus, 'form': form})
'''

def edu_list(request):
    form = RegionFilterForm(request.GET)
    if form.is_valid():
        region = form.cleaned_data['region']
        district = form.cleaned_data['district']
        edus = Edu.objects.all()
        if region:
            edus = edus.filter(region__icontains=region)
        if district:
            edus = edus.filter(district__icontains=district)
    else:
        edus = Edu.objects.all()
    return render(request, 'edu_list.html', {'edus': edus, 'form': form})